from rest_framework import serializers
from .models import *
from rest_framework.validators import UniqueValidator, UniqueTogetherValidator

class TagSerializer(serializers.ModelSerializer):
	class Meta:
		model = Tag
		fields = ['id', 'name']
		validators = [
			UniqueValidator(
				queryset=Tag.objects.all()
			)
		]


class CommentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Comment
		fields = ['id', 'text', 'user', 'article', 'response_to']


class FollowSerializer(serializers.ModelSerializer):
	class Meta:
		model = Follow
		fields = ['id', 'user', 'author']


class ArticleLikeSerializer(serializers.ModelSerializer):
	class Meta:
		model = ArticleLike
		fields = ['id', 'user', 'article', 'is_like']
		
		validators = [
			UniqueTogetherValidator(
				queryset=ArticleLike.objects.all(),
				fields=['user', 'article']
			)
		]


class BookmarkSerializer(serializers.ModelSerializer):
	class Meta:
		model = Bookmark
		fields = ['id', 'article', 'user']
		
		validators = [
			UniqueTogetherValidator(
				queryset=Bookmark.objects.all(),
				fields=['user', 'article']
			)
		]


class CommentLikeSerializer(serializers.ModelSerializer):
	class Meta:
		model = CommentLike
		fields = ['id', 'user', 'comment', 'is_like']
		
		validators = [
			UniqueTogetherValidator(
				queryset=CommentLike.objects.all(),
				fields=['user', 'comment']
			)
		]


class ArticleSerializer(serializers.ModelSerializer):
	tag = serializers.PrimaryKeyRelatedField(
		many=True,
		read_only=True,
		)
	class Meta:
		model = Article
		fields = ['id', 'author', 'title', 'text', 'is_valid', 'is_active',
				  'img_path', 'validator', 'val_date', 'tag', 'topic']



