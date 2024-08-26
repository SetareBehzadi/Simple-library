from django.urls import path

from book.views import BookListView

app_name = 'book'
urlpatterns = [
    path('', BookListView.as_view, name='books_list')
]