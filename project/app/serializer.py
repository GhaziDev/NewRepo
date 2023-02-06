from rest_framework import serializers
from app import models



class ArticleSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)
    class Meta:
        fields = 'slug','title','description',
        model = models.Article




