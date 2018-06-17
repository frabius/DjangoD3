from django.urls import path
from Diablo3_review import views
app_name = 'Diablo3_review'
urlpatterns = [
  path('', views.index, name='index'),
  path('article/<slug:slug>', views.article, name='article'),
  path('articles', views.articles, name='articles'),
]