from django.urls import path
from .views import blog_index, article_01 #article_02, article_03

urlpatterns = [
    path('', blog_index, name="blog_index"),
    path('article_<str:numero_article>', article_01, name="article_01"),
    #path('article_02', article_02, name="article_02"),
    #path('article_03', article_03, name="article_03"),
]
