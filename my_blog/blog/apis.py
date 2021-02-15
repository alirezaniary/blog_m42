from .models import Tag, BlogUser, Article, ArticleLike, Bookmark
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions, status
from django.db.models import Count
from django.shortcuts import get_object_or_404
from .serializers import *
from django.http import Http404



@api_view(['GET', 'POST'])
#@permission_classes((permissions.AllowAny,))
def tag_suggestion(request):
	if request.method == 'GET':
		print(request.query_params, type(request.query_params))
		tag = request.query_params['tag']								  
		queryset = Tag.objects.annotate(count=Count('article'))\
					  .filter(name__regex=r'.*' + tag + r'.*')\
					  .order_by('-count')[:5]
		serilizer = TagSerializer(queryset, many=True)
		return Response(serilizer.data)

	elif request.method == 'POST':
		queryset, _ = Tag.objects.get_or_create(name=request.data['tag'])
		serilizer = TagSerializer(queryset)
		return Response(serilizer.data)


@api_view(['GET', 'POST'])
def like_article(request):
	if request.method == 'POST':
		is_like = request.data['like'] == '1'
		user = get_object_or_404(BlogUser, pk=request.data['user'])
		article = get_object_or_404(Article, pk=request.data['article'])
		
		obj, created = ArticleLike.objects.get_or_create(article=article,
														 user=user,
														 defaults = {
														 'is_like': is_like})
		if not created:
			if obj.is_like == is_like:
				obj.delete()
			else:
				obj.is_like = is_like
				obj.save()

	
	elif request.method == 'GET':
		user = get_object_or_404(BlogUser, pk=request.query_params['user'])
		article = get_object_or_404(Article, pk=request.query_params['article'])
	
	return Response(article.user_like_status(user))
	

@api_view(['GET', 'POST'])
def bookmark_article(request):
	if request.method == 'GET':
		try:
			obj = get_object_or_404(Bookmark, article_id=request.query_params['article'],
											  user_id=request.query_params['user'])
			return Response({'bookmarked': True})
		except Http404:
			return Response({'bookmarked': False})
			
	elif request.method == 'POST':
		obj, created = Bookmark.objects.get_or_create(article_id=request.data['article'],
													  user_id=request.data['user'])
		if not created:
			obj.delete()
			return Response({'bookmarked': False})
		return Response({'bookmarked': True})
	
	
@api_view(['POST'])
def comment(request):
	serializer = CommentSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
		return Response(serializer.data, status=status.HTTP_201_CREATED)
	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	
	
	
	
	
	
	
	
	
	
