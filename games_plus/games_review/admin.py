from django.contrib import admin
from games_review.models import *

class GameAdmin(admin.ModelAdmin):
    list_display = ('name', 'release_date','picture' )
    search_fields = ('name', )
    list_filter = ('types', )


admin.site.register(Type)
admin.site.register(Game, GameAdmin)