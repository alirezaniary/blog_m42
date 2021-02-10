from .models import Tag
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from django.db.models import Count
from .serializers import *

@api_view(['GET', 'POST'])
#@permission_classes((permissions.AllowAny,))
def tag_suggestion(request):
	if request.method == 'GET':
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

