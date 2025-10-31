from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *
# Register your models here.
class LearnInline(admin.TabularInline):
    model = LearnOrder
    extra = 0

@admin.register(Order)
class OrderAdmin(ImportExportModelAdmin):
    list_display = ["user","description","create","paid"]
    inlines = [LearnInline]

@admin.register(OffCode)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["code","value","create","date_end"]