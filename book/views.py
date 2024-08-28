from django.shortcuts import redirect,render,HttpResponse,get_object_or_404
from django.views import View
from django.contrib.messages import Message


from book.models import Book


class BookListView(View):
    def get(self, request):
        books = Book.objects.exclude('status')
        return HttpResponse(books)

def books_list(request):
    books = Book.objects.exclude(status=4)
    return render(request, 'book/home.html', {'books':books})

def book_show(request, pk:int):
    book = Book.objects.get(id=pk)
    return render(request, 'book/show.html', {'book':book})

def book_delete(request, pk:int):
    book = get_object_or_404(Book, id=pk)
    book.delete()
    Message(request, 'Book is Deleted successfully', 'success')
    return redirect('book:books_list')

def book_create(request):
    pass