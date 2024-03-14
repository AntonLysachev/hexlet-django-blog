from django.urls import path
from hexlet_django_blog.article. views import IndexView, ArticleView, TegArticlePageView


urlpatterns = [
    path('', IndexView.as_view(), name='article'),
    path('<int:id>/', ArticleView.as_view(), name='article_id'),
    # path('<int:article_id>/comments/<int:id>/', ArticleCommentsView.as_view(), name='article_comments'),
    path('<slug:tag_id>/<int:article_id>/', TegArticlePageView.as_view(template_name='tag_article.html'), name='tag_article'),
]
