from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.
class Book(models.Model):
    desk = models.TextField()
    link = models.CharField(max_length=255)
    name = models.CharField(max_length=125)
    author = models.CharField(max_length=255)
    allowedsub_id = models.ForeignKey('Allowedsub', on_delete=models.CASCADE)
    review_id = models.ForeignKey('Review', on_delete=models.CASCADE)
    tag_id = models.ForeignKey('Tag', on_delete=models.CASCADE)


class Review(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()


class Tag(models.Model):
    name = models.CharField(max_length=255)


class Allowedsub(models.Model):
    PLAN_TYPE_CHOICES = (
        ('classic', 'Classic'),
        ('student', 'Student'),
        ('premium', 'Premium'),
    )


#Это уже модуль подписок


