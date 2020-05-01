from django import forms
from .models import Notes


class BlogForm(forms.ModelForm):
  class Meta:
    model = Notes
    fields = ['title' , 'content' , 'tages']