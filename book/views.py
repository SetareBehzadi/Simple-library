from django.shortcuts import redirect,render,HttpResponse,get_object_or_404
from django.views import View
from django.contrib import messages

from book.forms import BookCreateForm
from book.models import Book, Author, Category


class BookListView(View):
    def get(self, request):
        books = Book.objects.exclude(status=4)
        query = request.GET.get('q')
        # print('**'*4)
        # print(query)
        if query:
            books = books.filter(author__name__contains=query) | books.filter(title__contains=query)
        return render(request, 'book/home.html', {'books': books})


def book_show(request, pk:int):
    book = Book.objects.get(id=pk)
    return render(request, 'book/show.html', {'book':book})

def book_delete(request, pk:int):
    book = get_object_or_404(Book, id=pk)
    book.delete()
    messages.success(request, 'Book is Deleted successfully', 'success')
    return redirect('book:books_list')


class BookCreateView(View):
    form_class = BookCreateForm
    template_name = 'book/create.html'
    def get(self, request):
        form = self.form_class
        return render(request, self.template_name , {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            print("333"*10)
            print(cd)
            author_instance = get_object_or_404(Author, name=cd['author'])
            category_instance = get_object_or_404(Category, name=cd['category'])
            Book.objects.create(title=cd['title'], description=cd['description'], published_date=cd['published_date'],
                                author=author_instance, category=category_instance, price=cd['price'], status=cd['status'])

            messages.success(request, 'todo is added successfully', 'success')
            return redirect('book:books_list')

class BookEditeView(View):
    form_class = BookCreateForm
    template_name = 'book/create.html'
    def setup(self, request, *args, **kwargs):
        print("sssssssssssssssssssssssssss")
        print(kwargs)
        print(args)
        print(request)
        self.book_instance =  get_object_or_404(Book, id=kwargs['pk'])
        return super().setup(request, *args, **kwargs)

    def get(self, request, pk):
        book = self.book_instance
        form = self.form_class(instance=book)
        return render(request, self.template_name, {'form': form})

    def post(self, request, pk):
        form = self.form_class(request.POST,instance=self.book_instance)
        if form.is_valid:
            newBook = form.save()
        messages.success(request, 'update successfully', 'success')
        return redirect('book:books_list')

