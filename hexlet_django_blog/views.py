from typing import Any
from django.http import HttpRequest
from django.views.generic.base import TemplateView
from django.urls import reverse
from django.shortcuts import redirect
from django.http.response import HttpResponse

TAGS = ['обучение', 'программирование', 'python', 'oop']


class IndexPageView(TemplateView):
    template_name = "index.html"
    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        return redirect(reverse('tag_article', kwargs={'tag_id': 'python', 'article_id': 42}))


class aboutPageView(TemplateView):
    template_name='about.html'
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        return{'tags': TAGS}

