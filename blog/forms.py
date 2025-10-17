from django import forms
from .models import *
from django_ckeditor_5.widgets import CKEditor5Widget

class PostForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditor5Widget)

    class Meta:
        model = Post
        fields = ["title","summery_description","body"]

