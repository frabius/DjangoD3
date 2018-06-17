from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Type(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField()
    class Meta:
        verbose_name = 'Catégorie'
        verbose_name_plural = 'Catégories'


class MyArticle(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    release_date = models.DateTimeField(auto_now_add=True)
    picture = models.ImageField()
    types = models.ManyToManyField(Type)
    description= models.CharField(max_length=500)

    def  __str__(self):
        return self.name

class Commentaire(models.Model):
    description= models.CharField(max_length=500)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    release_date = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(MyArticle, on_delete=models.CASCADE, related_name="commentaires")

    def  __str__(self):
        return self.description
