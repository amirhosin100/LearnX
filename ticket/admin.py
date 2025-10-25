from django.contrib import admin
from .models import *
# Register your models here.
class AnswerInline(admin.TabularInline):
    model = AnswerTicket
    extra = 0
    ordering = ["create"]


@admin.register(SimpleTicket)
class SimpleTicketAdmin(admin.ModelAdmin):
    list_display = ["user","title","category","create"]
    inlines = [AnswerInline]

@admin.register(CollaborationTicket)
class CollaborationTicketAdmin(admin.ModelAdmin):
    list_display = ["user","first_name","last_name","city","phone"]