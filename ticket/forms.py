from django import forms
from .models import SimpleTicket,TeacherTicket

class SimpleTicketForm(forms.ModelForm):
    class Meta :
        model = SimpleTicket
        fields = ["category","message"]

class TeacherTicketForm(forms.ModelForm):
    class Meta :
        model = TeacherTicket
        fields = ["first_name","last_name","age","city","address","phone","bio"]

    def clean_bio(self):
        bio = self.cleaned_data["bio"]
        if len(bio) < 50 :
            raise forms.ValidationError("توضیحات درباره خودتان کم است")
        else:
            return bio