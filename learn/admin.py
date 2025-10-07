from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Learn)
class LearnAdmin(admin.ModelAdmin):
    list_display = ["teacher","title","create"]

@admin.register(Headline)
class HeadlineAdmin(admin.ModelAdmin):
    list_display = ["learn","title","create"]

@admin.register(LearnFilms)
class LearnFilmsAdmin(admin.ModelAdmin):
    list_display = ["headline","title","film"]

@admin.register(FilmScores)
class FilmScoresAdmin(admin.ModelAdmin):
    list_display = ["user_from","film_to","score"]