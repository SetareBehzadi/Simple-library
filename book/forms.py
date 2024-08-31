from django import forms

from book.models import Author, Book


class BookAuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        exclude = ['created_at', 'updated_at']


class BookCreateForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude =['created_at','updated_at']
        widgets = {
            'description': forms.Textarea(attrs={'col':3, 'row':5, 'class': 'form-control'}),
            'published_date': forms.DateInput(attrs={'type':'date'})
        }


class BookFilterForm(forms.Form):
    min_price = forms.IntegerField(
        required=False,
        min_value=0,
        label='Min Price',
        widget=forms.NumberInput(attrs={'class': 'form-control lg-4 mb-4', 'placeholder': 'Min Price'})
    )
    max_price = forms.IntegerField(
        required=False,
        min_value=0,
        label='Max Price',
        widget=forms.NumberInput(attrs={'class': 'form-control mb-4', 'placeholder': 'Max Price'})
    )
    start_date = forms.DateField(
        required=False,
        label='Start Date',
        widget=forms.DateInput(attrs={'class': 'form-control mb-2', 'type': 'date', 'placeholder': 'Start Date'})
    )
    end_date = forms.DateField(
        required=False,
        label='End Date',
        widget=forms.DateInput(attrs={'class': 'form-control mb-2', 'type': 'date', 'placeholder': 'End Date'})
    )