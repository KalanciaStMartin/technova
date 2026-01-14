from django.shortcuts import render, get_object_or_404
from .models import Article

def liste_articles(request):
    articles = Article.objects.filter(publie=True)
    return render(request, 'blog/liste.html', {'articles': articles})

def detail_article(request, slug):
    article = get_object_or_404(Article, slug=slug, publie=True)
    article.vues += 1
    article.save()
    return render(request, 'blog/detail.html', {'article': article})