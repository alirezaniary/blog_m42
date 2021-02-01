from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, ArticleCreationForm


def index(request):
	return render(request, 'index.html')

def signup(request):
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
    return render(request, 'signup.html', {'form': form})

def new_article(request):
    if request.method == 'POST':
        form = ArticleCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:index')
    else:
        form = ArticleCreationForm()
    return render(request, 'new_article.html', {'form': form})
