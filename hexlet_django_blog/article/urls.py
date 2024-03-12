from django.urls import path

from hexlet_django_blog.article import views

urlpatterns = [
    path('', views.ArticlePageView.as_view(template_name='articles.html'), name='article'),
    path('<slug:tag_id>/<int:article_id>/', views.TegArticlePageView.as_view(template_name='tag_article.html'), name='tag_article')
]