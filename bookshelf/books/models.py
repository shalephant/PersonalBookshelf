from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    country = models.CharField(max_length=30)
    birth = models.DateField()
    death = models.DateField(null=True, blank=True)

class Book(models.Model):
    title = models.CharField(max_length=100)
    year = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField()
