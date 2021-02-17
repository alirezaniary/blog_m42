from rest_framework import serializers
from .models import Tag, Comment, Follow
import json

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
    	model = Comment
    	fields = ['id', 'text', 'user', 'article', 'response_to']


class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = ['id', 'user', 'author']
