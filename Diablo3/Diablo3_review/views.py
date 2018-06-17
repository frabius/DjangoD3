from django.shortcuts import render
from Diablo3_review.models import *
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from Diablo3_review.form import CommentaireForm
from .filters import *
import datetime
from django.utils import timezone


# Create your views here.
def index(request):
    article = MyArticle.objects.all()
    article_filtre = articleFilter(request.GET,queryset=article)
    return render(request, 'index.html', {'article_filtre': article_filtre})

def article(request,slug):
    article = get_object_or_404(MyArticle, slug=slug)
    if request.method == "POST":
        form = CommentaireForm(request.POST)
        if form.is_valid():
            article.commentaires.create(description = form.cleaned_data['description'],author = request.user , release_date = datetime.datetime.today())
    form = CommentaireForm()
    return render(request, 'article.html', {'article': article,'form':form,})

def articles(request):
    articles = MyArticle.objects.order_by('id').all()
    paginator =Paginator(articles,3)
    page = request.GET.get('page')
    try:
        articlepage = paginator.page(page)
    except PageNotAnInteger:
        articlepage = paginator.page(1)
    except EmptyPage:
        articlepage = paginator.page(paginator.num_pages)
    
    
    return render(request, 'articles.html', {'articles': articlepage})


