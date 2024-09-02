from django.contrib import admin

from service.feed.books.models import Book, Review, Tag, Allowedsub

# Register your models here.
admin.site.register(Book)
admin.site.register(Review)
admin.site.register(Tag)
admin.site.register(Allowedsub)
