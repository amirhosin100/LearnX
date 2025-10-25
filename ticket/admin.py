from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(SimpleTicket)
class SimpleTicketAdmin(admin.ModelAdmin):
    list_display = ["user","category","message","create"]

@admin.register(TeacherTicket)
class TeacherTicketAdmin(admin.ModelAdmin):
    list_display = ["user","first_name","last_name","city","phone"]