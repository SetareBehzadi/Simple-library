from cProfile import label

from django import forms

from book.models import Status, Author, Category, Book


class BookAuthorForm(forms.ModelForm):
    # name = forms.CharField(label="Author Name")
    class Meta:
        model = Author
        exclude = ['created_at', 'updated_at']


class BookCreateForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude =['created_at','updated_at']
        widgets = {
            'description': forms.Textarea(attrs={'col':3, 'row':5, 'class': 'form-control'})
        }