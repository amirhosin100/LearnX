from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
# Register your models here.

@admin.register(User)
class UserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("موارد اضافه", {"fields": ("job","bio","image")}),
    )

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ["user","phone_number","address"]
    search_fields = ["city","phone_number"]
    ordering = ["-join"]

@admin.register(Bloger)
class BlogerAdmin(admin.ModelAdmin):
    list_display = ["user","phone_number","address"]
    search_fields = ["city","phone_number"]
    ordering = ["-join"]