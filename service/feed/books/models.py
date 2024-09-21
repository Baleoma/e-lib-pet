from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.
class Book(models.Model):
    desk = models.TextField()
    link = models.CharField(max_length=255)
    name = models.CharField(max_length=125)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    sub_id = models.ForeignKey('Sub', on_delete=models.CASCADE)
    tag_id = models.ForeignKey('Tag', on_delete=models.CASCADE)


class Review(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    book_id = models.ForeignKey('Book', on_delete=models.CASCADE)


class Tag(models.Model):
    name = models.CharField(max_length=255)


class Sub(models.Model):
    name = models.CharField(max_length=255)







#Это уже модуль подписок


