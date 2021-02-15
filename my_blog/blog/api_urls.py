from django.urls import path
from blog.apis import *

urlpatterns = [
	path('tag/', tag_suggestion),
	path('like/', like_article),
	path('bookmark/', bookmark_article),
	path('comment/', comment),
]

