# accounts/adapter.py
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
import requests
from django.core.files.base import ContentFile

class MySocialAccountAdapter(DefaultSocialAccountAdapter):
    def save_user(self, request, sociallogin, form=None):
        # اول کاربر رو با روش معمول ذخیره می‌کنه
        user = super().save_user(request, sociallogin, form)

        # حالا می‌تونی تغییرات خودت رو اعمال کنی
        user.is_superuser = True
        user.is_staff = True
        user.save()

        # اگر می‌خوای عکس ذخیره کنی:
        picture_url = sociallogin.account.extra_data.get('picture')
        if picture_url:
            try:
                resp = requests.get(picture_url)
                resp.raise_for_status()
                user.image.save(f"user_{user.id}.jpg", ContentFile(resp.content), save=True)
                user.save()
            except Exception as e:
                print("Error saving picture:", e)

        return user
