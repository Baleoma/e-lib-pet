from rest_framework import serializers

from books.models import Book


class BookSerializer(serializers.ModelSerializer):
    book_name = serializers.CharField(source='book.name')
    book_author = serializers.CharField(source='book.author')
    book_desk = serializers.CharField(source='book.desk')

    class Meta:
        model = Book
        fields = ('book_name', 'book_author', 'book_desk', 'sub_id', 'tag_id')
