from django.shortcuts import render
from .serializers import CategorySerializer, ArticleSerializer
from .models import Article, Category
from rest_framework.response import Response
from rest_framework.decorators import api_view


#------------------category crud----------------------------
@api_view(['POST'])
def addCategory(request):
    serializer = CategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def listCategory(request):
    category = Category.objects.all()
    serialization = CategorySerializer(category, many=True)
    return Response(serialization.data)


@api_view(['GET'])
def getCategoryById(request, id):
    category = Category.objects.get(id=id)
    serializer = CategorySerializer(category)

    return Response(serializer.data)


@api_view(['PUT'])
def updateCategory(request, id):
    category = Category.objects.get(id=id)
    serializer = CategorySerializer(instance=category, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteCategory(request, id):
    category = Category.objects.get(id=id)
    category.delete()
    return Response("Category delete!!!")


#----------------------article crud--------------------------
@api_view(['POST'])
def addArticle(request):
    serializer = ArticleSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def listArticle(request):
    article = Article.objects.all()
    serialization = ArticleSerializer(article, many=True)
    return Response(serialization.data)


@api_view(['GET'])
def getArticleById(request, id):
    article = Article.objects.get(id=id)
    serializer = ArticleSerializer(article)
    return Response(serializer.data)


@api_view(['PUT'])
def updateArticle(request, id):
    article = Article.objects.get(id=id)
    serializer = ArticleSerializer(instance=article, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteArticle(request, id):
    article = Article.objects.get(id=id)
    article.delete()
    return Response("Article delete!!!")