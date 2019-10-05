from django.contrib import admin
from blogsite.models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'pub_time')


admin.site.register(Article, ArticleAdmin)
