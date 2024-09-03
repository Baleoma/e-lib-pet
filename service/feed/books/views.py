from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet

from books.models import Book
from books.serializers import BookSerializer


# Create your views here.
class BooksView(ReadOnlyModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
