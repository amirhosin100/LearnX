from django.contrib import admin
from .models import *
# Register your models here.
class LearnInline(admin.TabularInline):
    model = LearnOrder
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["user","description","create","paid"]
    inlines = [LearnInline]

@admin.register(OffCode)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["code","value","create","date_end"]