from typing import Any
from django.views import View
from django.views.generic.base import TemplateView
from hexlet_django_blog.article.models import Article
from django.shortcuts import render, get_object_or_404


class IndexView(View):

    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(request, 'articles/index.html', context={
            'articles': articles,
        })
   

class TegArticlePageView(TemplateView):

    template_name = "tags_article_id"

    def get_context_data(self, tag_id, article_id) -> dict[str, Any]:
        return {'tag_id': tag_id, 'article_id': article_id}


class ArticleView(View):

    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['id'])
        return render(request, 'articles/show.html', context={
            'article': article,
        })

# class ArticleCommentsView(View):

#     def get(self, request, *args, **kwargs):
#         comment = get_object_or_404(Comment, id=kwargs['id'], article__id=kwargs['article_id'])

#         return render( ... )
