from rest_framework import serializers
from .models import Tag, Comment
import json

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
    	model = Comment
    	fields = ['id', 'text', 'user', 'article', 'response_to']

       
