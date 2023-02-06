from django.db import models
from django.template.defaultfilters import slugify  # new


class Article(models.Model):
    slug = models.SlugField(primary_key=True,unique=True)
    title = models.CharField(max_length=200)
    description = models.TextField()

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            super().save(*args,**kwargs)
    




# Create your models here.
