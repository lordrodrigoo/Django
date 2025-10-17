from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from tag.models import Tag
from ..serializers import TagSerializer
from rest_framework import status

from ..models import Recipe
from ..serializers import RecipeSerializer

@api_view(http_method_names=['GET', 'POST'])
def recipe_api_list(request):

    if request.method == 'GET':
        recipes = Recipe.objects.get_published()
        serializer = RecipeSerializer(
            instance=recipes,
            many=True,
            context={'request': request},
        )
        return Response(serializer.data)
    elif request.method == 'POST':
        return Response('POST', status=status.HTTP_201_CREATED)

@api_view()
def recipe_api_detail(request, pk):
    recipe = get_object_or_404(
        Recipe.objects.get_published(),
        pk=pk,
        
    )
    serializer = RecipeSerializer(
        instance=recipe,
          many=False,
          context={'request': request},
    )

    return Response(serializer.data)

@api_view()
def tag_api_detail(request, pk):
    tag = get_object_or_404(
        Tag.objects.all(),
        pk=pk,
        
    )
    serializer = TagSerializer(
        instance=tag,
        many=False,
        context={'request': request},
    )

    return Response(serializer.data)
    return Response(True)