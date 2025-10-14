from django import forms
from .models import *


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ["first_name","last_name",'username','email']

    def clean_password2(self):
        password = self.cleaned_data["password"]
        password_2 = self.cleaned_data["password2"]

        if password != password_2 :
            raise forms.ValidationError("پسورد ها مطابقت ندارند")
        else:
            return password_2

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("ایمیل از قبل وجود دارد")
        else:
            return email
    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("این نام کاربری از قبل وجود دارد")
        else:
            return username

class EditUserForm(forms.ModelForm):

    class Meta :
        model = User
        fields = ["first_name","last_name","email","bio","job","image"]
