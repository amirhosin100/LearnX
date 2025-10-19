from django import forms
from .models import *
from django_ckeditor_5.widgets import CKEditor5Widget

class LearnForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditor5Widget(config_name="learn"))
    class Meta :
        model = Learn
        fields = ["title","slug","image","summery_description","description","learn_time",
                  "price","precent_off"]
