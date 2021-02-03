from django.urls import path, re_path
from django.views.static import serve
from . import views
from django.conf import settings

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('new/', views.new_article, name='new_article'),
    path('@<username>/<article_id>/', views.show_article, name='article'),

]


if settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]