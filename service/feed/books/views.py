from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet

from books.models import Book, Review
from books.serializers import BookSerializer, ReviewSerializer


# Create your views here.
class BooksView(ReadOnlyModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class ReviewView(ReadOnlyModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
