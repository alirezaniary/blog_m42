from django.urls import path, include
from blog.APIs import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('like', ArticleLikeViewSet)
router.register('clike', CommentLikeViewSet)
router.register('bookmark', BookmarkViewSet)
router.register('comment', CommentViewSet)
router.register('article', ArticleViewSet)
router.register('follow', FollowViewSet)


urlpatterns = [
	path('', include(router.urls)),
	path('tag/', ListCreateTag.as_view()),
	path('author/<int:pk>/', RetrieveAuthor.as_view()),
	path('search/', listArticle.as_view()),
]

