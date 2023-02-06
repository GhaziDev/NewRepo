from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from app import models
from app import serializer


class ArticleView(ModelViewSet):
    serializer_class = serializer.ArticleSerializer
    def get_queryset(self):
        return models.Article.objects.all()
    
    def post(self,request):
        data = serializer.ArticleSerializer(data=request.data)

        if data.is_valid():

            a = models.Article.objects.create(title=data['title'],description=data['description'])
            a.save()
            return Response("succes",status=200)
        return Response("fail",status=400)




# Create your views here.
