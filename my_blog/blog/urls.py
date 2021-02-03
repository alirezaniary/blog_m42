from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('new/', views.new_article, name='new_article'),
    path('@<username>/<article_id>/', views.show_article, name='article'),
]
