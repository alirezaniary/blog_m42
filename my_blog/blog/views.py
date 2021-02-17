from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, ArticleCreationForm, CommentForm
from django.views import generic
from .models import BlogUser, Article, Topic, Tag



topic_list = Topic.objects.filter(super_topic=None)

def index(request):
    return render(request, 'index.html',{'topic_list': topic_list,
    									 'article': Article.objects.all(),
                                         })


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('blog:index')
    else:
        form = SignUpForm()
    return render(request, 'sign_up.html', {'form': form,
                                            'topic_list': topic_list
                                            })


def new_article(request):
    if request.method == 'POST':
        article_form = ArticleCreationForm(request.POST, request.FILES)

        if article_form.is_valid():
            article = article_form.save(commit=False)
            article.author_id = request.user.bloguser.id
            article.save()
            article_form.save_m2m()
            return redirect('blog:article',
            				article_id=article.id,
            				username=request.user.username)
        else:
            render(request, 'new_article.html', {'form': article_form,
                                                'topic_list': topic_list,
                                                })
    elif request.method == 'GET':
        article_form = ArticleCreationForm()
    return render(request, 'new_article.html', {'form': article_form,
                                                'topic_list': topic_list,

                                                })


def show_article(request, username, article_id):
	article = get_object_or_404(
	    Article, pk=article_id, author__username=username)
	author = article.author
	comments = article.comment_set.filter(response_to=None)
	article_count = author.published.filter(is_valid=True).count()
	follower_count = author.followedBy.count()
	comment_form = CommentForm()
	return render(request, 'show_article.html', {'author': author, 
	                                             'article': article,
	                                             'article_count': article_count,
	                                             'follower_count': follower_count,
	                                             'topic_list': topic_list, 
	                                             'form': comment_form,
	                                             'comments': comments,
	                                             'data': {'article': article.id,
	                                             		  'author': author.id,	                                             
	                                                      'user': request.user.bloguser.id}
	                                             })

def show_tag(request, tag_name):
	tag = get_object_or_404(Tag, name=tag_name)
	return render(request, 'index.html',{'topic_list': topic_list,
    									 'article': Article.objects.filter(tag__name=tag_name),
    									 'title': tag
                                         })


def show_topic(request, topic_name):
	topic = get_object_or_404(Topic, name=topic_name)
	return render(request, 'index.html',{'topic_list': topic_list,
    									 'article': Article.objects.filter(topic__name=topic_name),
    									 'title': topic,
                                         })













