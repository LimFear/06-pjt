from django import forms
from .models import Book, Thread

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'description', 'score', 'author')

class ThreadForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ('title', 'content', 'read_date')
        widgets = {
            'read_date': forms.DateInput(attrs={'type': 'date'}),
        }
