# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ArticleSerializer
from .models import Article

def home(request):
	return render(request,'index.html',{})

@api_view(["POST"])
def create_article(request):
    serializer = ArticleSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "success"}) 
    else:
        data = {
          "error": True,
          "message": serializer.errors,          
        }
        return Response(data)        

@api_view(["GET"])
def view_articles(request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def like_article(request,id):
	try:
	    article = Article.objects.get(id=id)
	    article.likes+=1
	    article.save()
	    data = {
          "error": False,
          "message": "success", 
          "likes": article.likes,        
        }
	    return Response(data)
	except:
          data = {
              "error": True,
              "message": "Article not found",          
            }
          return Response(data) 
    