from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, ArticleCreationForm
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
        form = ArticleCreationForm(request.POST, request.FILES)

        if form.is_valid():
            article = form.save()
            print(article)
            id = article.id
            print(id)
            un = article.author.username
            print(un)
            return redirect('blog:article', article_id=id, username=un)
        else:
            render(request, 'new_article.html', {'form': form,
                                                'topics': topics,
                                                })
    else:
        form = ArticleCreationForm()
    return render(request, 'new_article.html', {'form': form,
                                                'topics': topics,

                                                })


def show_article(request, username, article_id):
    article = get_object_or_404(
        Article, pk=article_id, author__username=username)
    user = get_object_or_404(BlogUser, username=username)
    article_count = user.published.filter(is_valid=True).count()
    follower_count = user.followedBy.count()
    return render(request, 'show_article.html', {'blog_user': user, 
                                                 'article': article,
                                                 'article_count': article_count,
                                                 'follower_count': follower_count,
                                                 'topics': topics,
                                                 })
