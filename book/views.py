from django.shortcuts import redirect,render,HttpResponse,get_object_or_404
from django.views import View
from django.contrib import messages

from book.forms import BookCreateForm, BookFilterForm
from book.models import Book, Author, Category


class BookListView(View):
    def get(self, request):
        books = Book.objects.exclude(status=4)
        filter_form = BookFilterForm(request.GET)
        query = request.GET.get('q')
        if query:
            books = books.filter(author__name__contains=query) | books.filter(title__contains=query)

        if filter_form.is_valid():
            cd = filter_form.cleaned_data
            min_price = cd['min_price']
            max_price = cd['max_price']
            start_date = cd['start_date']
            end_date = cd['end_date']

            if min_price is not None:
                books = books.filter(price__gte=min_price)
            if max_price is not None:
                books = books.filter(price__lte=max_price)

            if start_date:
                books = books.filter(published_date__gte=start_date)
            if end_date:
                books = books.filter(published_date__lte=end_date)
        return render(request, 'book/home.html', {'books': books, 'form':filter_form})

    def post(self, request):
        books_id = request.POST.getlist('book_ids')
        if books_id:
            Book.objects.filter(id__in=books_id).delete()
        return redirect('book:books_list')



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

