from django import forms
from django.forms import ModelForm
from .models import AuthorModel,BookModel

class AuthorForm(ModelForm):
    class Meta:
        model = AuthorModel
        fields = ['First_Name','Last_Name','Address']
class BookForm(ModelForm):
    class Meta:
        model = BookModel
        fields = ['Title','Author','Publication_Year','ISBN','Price']