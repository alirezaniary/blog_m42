from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, ArticleCreationForm, CommentForm
from django.views import generic
from .models import BlogUser, Article, Topic

topics = Topic.objects.all()

def index(request):
    return render(request, 'index.html',{'topics': topics,
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
                                            'topics': topics
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
                                                'topics': topics,
                                                })
    elif request.method == 'GET':
        article_form = ArticleCreationForm()
    return render(request, 'new_article.html', {'form': article_form,
                                                'topics': topics,

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
	                                             'topics': topics, 
	                                             'form': comment_form,
	                                             'comments': comments,
	                                             'data': {'article': article.id,
	                                             		  'author': author.id,	                                             
	                                                      'user': request.user.bloguser.id}
	                                             })

	













