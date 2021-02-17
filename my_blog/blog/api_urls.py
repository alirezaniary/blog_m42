from django.urls import path
from blog.apis import *

urlpatterns = [
	path('tag/', tag_suggestion),
	path('like/', like_article),
	path('clike/', like_comment),
	path('bookmark/', bookmark_article),
	path('comment/', send_comment),
	path('follow/', follow_author),
]

