from django.urls import path

from book.views import BookListView,books_list,book_create,book_show,book_delete

app_name = 'book'
urlpatterns = [
    # path('', BookListView.as_view(), name='books_list')
    path('', books_list, name='books_list'),
    path('show/<int:pk>/', book_show, name='book_show'),
    path('delete/<int:pk>/', book_delete, name='book_delete'),
    path('create/', book_create, name='book_create'),
]