from django.contrib import admin

from django.contrib import admin
from Diablo3_review.models import *


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name', 'release_date', )
    search_fields = ('name', )
    list_filter = ('types', )

# Register your models here.

admin.site.register(Type)
admin.site.register(MyArticle , ArticleAdmin)
admin.site.register(Commentaire)
