from .serializers import *
from .models import *
from rest_framework import generics, permissions, status
from django.db.models import Count
from rest_framework import mixins
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.response import Response



class ListCreateTag(generics.ListCreateAPIView):
	serializer_class = TagSerializer
	permission_classes = [permissions.IsAuthenticated]

	def get_queryset(self):
		tag = self.request.query_params.get('name', None)
		queryset = Tag.objects.all()
		if tag is not None:
			return queryset.annotate(count=Count('article'))\
						   .filter(name__regex=r'.*' + tag + r'.*')\
						   .order_by('-count')[:5]
		return queryset


class ArticleLikeViewSet(mixins.CreateModelMixin,
						 mixins.UpdateModelMixin,
						 mixins.DestroyModelMixin,
						 mixins.RetrieveModelMixin,
						 viewsets.GenericViewSet):
	queryset = ArticleLike.objects.all()
	serializer_class = ArticleLikeSerializer
	permission_classes = [permissions.IsAuthenticated]
	
	def get_object(self):
		queryset = self.get_queryset()
		filter = {}
		for field in ['user', 'article']:
			filter[field] = self.request.query_params.get(field)

		obj = get_object_or_404(queryset, **filter)		
		self.check_object_permissions(self.request, obj)
		return obj



class CommentLikeViewSet(mixins.CreateModelMixin,
						 mixins.UpdateModelMixin,
						 mixins.DestroyModelMixin,
						 viewsets.GenericViewSet):
	queryset = CommentLike.objects.all()
	serializer_class = CommentLikeSerializer
	permission_classes = [permissions.IsAuthenticated]
	
	def get_object(self):
		queryset = self.get_queryset()
		filter = {}
		for field in ['user', 'comment']:
			filter[field] = self.request.query_params.get(field)

		obj = get_object_or_404(queryset, **filter)		
		self.check_object_permissions(self.request, obj)
		return obj
		

class BookmarkViewSet(mixins.CreateModelMixin,
					  mixins.DestroyModelMixin,
					  mixins.RetrieveModelMixin,
					  viewsets.GenericViewSet):
	queryset = Bookmark.objects.all()
	serializer_class = BookmarkSerializer
	permission_classes = [permissions.IsAuthenticated]
	
	def get_object(self):
		queryset = self.get_queryset()
		filter = {}
		for field in ['user', 'article']:
			filter[field] = self.request.query_params.get(field)

		obj = get_object_or_404(queryset, **filter)		
		self.check_object_permissions(self.request, obj)
		return obj


class FollowViewSet(mixins.CreateModelMixin,
					mixins.DestroyModelMixin,
					mixins.RetrieveModelMixin,
					viewsets.GenericViewSet):
	queryset = Follow.objects.all()
	serializer_class = FollowSerializer
	permission_classes = [permissions.IsAuthenticated]
	
	def get_object(self):
		queryset = self.get_queryset()
		filter = {}
		for field in ['user', 'author']:
			filter[field] = self.request.query_params.get(field)

		obj = get_object_or_404(queryset, **filter)		
		self.check_object_permissions(self.request, obj)
		return obj


class CommentViewSet(mixins.CreateModelMixin,
					 mixins.UpdateModelMixin,
					 mixins.ListModelMixin,
					 mixins.RetrieveModelMixin,
					 viewsets.GenericViewSet):
	queryset = Comment.objects.all()
	serializer_class = CommentSerializer
	permission_classes = [permissions.IsAuthenticated, ]


class ArticleViewSet(mixins.UpdateModelMixin,
					 mixins.ListModelMixin,
					 mixins.RetrieveModelMixin,
					 viewsets.GenericViewSet):
	queryset = Article.objects.all()
	serializer_class = ArticleSerializer
	permission_classes = [permissions.IsAuthenticated, ]








