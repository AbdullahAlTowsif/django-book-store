from django import forms
from book.models import BookStoreModel
class BookStoreForm(forms.ModelForm):
    class Meta:
        model = BookStoreModel
        fields = '__all__'