from rest_framework import serializers

from books.models import Book, Sub, Review


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('name', 'author', 'desk', 'sub_id', 'tag_id')


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('username', 'content', 'book_id')
