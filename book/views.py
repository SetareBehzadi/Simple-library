from django.shortcuts import render,HttpResponse
from django.views import View

from book.models import Book


class BookListView(View):
    def get(self, request):
        books = Book.objects.exclude('status')
        return HttpResponse(books)
