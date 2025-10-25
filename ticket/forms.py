from django import forms
from .models import *

class SimpleTicketForm(forms.ModelForm):
    class Meta :
        model = SimpleTicket
        fields = ["title","category"]

class AnswerTicketForm(forms.ModelForm):
    class Meta :
        model = AnswerTicket
        fields = ["message"]


class CollaborationTicketForm(forms.ModelForm):
    class Meta :
        model = CollaborationTicket
        fields = ["first_name","last_name","type","age","city","address","phone","bio"]

    def clean_bio(self):
        bio = self.cleaned_data["bio"]
        if len(bio) < 50 :
            raise forms.ValidationError("توضیحات درباره خودتان کم است")
        else:
            return bio
    def clean_address(self):
        address = self.cleaned_data["address"]
        if len(address) < 20 :
            raise forms.ValidationError("آدرس بسیار کوتاه است")
        else:
            return address