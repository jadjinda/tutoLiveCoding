from django.db import models


class Category(models.Model):
    libelle = models.CharField(max_length=60)


class Article(models.Model):
    titre = models.CharField(max_length=60)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(max_length=100)
