from typing import Any
from django.views import View
from django.views.generic.base import TemplateView
from hexlet_django_blog.article.models import Article
from django.shortcuts import render

# TEAM = [
#     {'name': 'Yoda', 'position': 'CEO'},
#     {'name': 'Obi-Wan Kenobi', 'position': 'Senior Developer'},
#     {'name': 'Anakin Skywalker', 'position': 'Junior Developer'},
#     {'name': 'Jar Jar Binks', 'position': 'Trainee'},
# ]


# class ArticlePageView(TemplateView):

#     template_name = "articles.html"

#     def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
#         return {'body': TEAM,}
    

class TegArticlePageView(TemplateView):

    template_name = "tags_article_id"

    def get_context_data(self, tag_id, article_id) -> dict[str, Any]:
        return {'tag_id': tag_id, 'article_id': article_id}


class IndexView(View):

    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(request, 'articles/index.html', context={
            'articles': articles,
        })