from django.urls import path
from games_review import views
app_name = 'games_review'
urlpatterns = [
    path('', views.index, name='index'),
    path('jeu/<slug:slug>', views.game, name='game'),
]