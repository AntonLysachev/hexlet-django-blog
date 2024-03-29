from django.contrib import admin
from .models import Article
from django.contrib.admin import DateFieldListFilter


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    search_fields = ['name', 'body']
    list_display = ('id', 'name', 'timestamp')
    list_filter = (('timestamp', DateFieldListFilter),)
