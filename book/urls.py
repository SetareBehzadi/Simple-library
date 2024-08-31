from django.urls import path

from book.views import BookListView, BookCreateView, book_show, book_delete, BookEditeView

app_name = 'book'
urlpatterns = [
    # path('', BookListView.as_view(), name='books_list')
    path('', BookListView.as_view(), name='books_list'),
    path('create/', BookCreateView.as_view(), name='book_create'),
    # path('search/', name='search_books'),
    path('show/<int:pk>/', book_show, name='book_show'),
    path('edite/<int:pk>/', BookEditeView.as_view(), name='book_edit'),
    path('delete/<int:pk>/', book_delete, name='book_delete'),
]