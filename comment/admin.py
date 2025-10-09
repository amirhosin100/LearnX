from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(CommentForLearn)
class CommentForLearnAdmin(admin.ModelAdmin):
    list_display = ["user","learn","content"]
    list_filter = ["create"]

@admin.register(AskForFilm)
class AskForFilmAdmin(admin.ModelAdmin):
    list_display = ["user","film","content"]
    list_filter = ["create"]

@admin.register(AnswerForFilm)
class AnswerForFilmAdmin(admin.ModelAdmin):
    list_display = ["user","ask","content"]
    list_filter = ["create"]