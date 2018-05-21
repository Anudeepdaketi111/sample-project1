from django.conf.urls import url
from .views import *
from django.views.generic.base import TemplateView
urlpatterns = [

    
    url(r'^$', TemplateView.as_view(template_name='index.html'), name="home"),
    url(r'^new_article/$', TemplateView.as_view(template_name='new_article.html'), name="new_article"), 
    url(r'^view_articles/$', view_articles, name="view_articles"),
    url(r'^create_article/$', create_article, name="create_article"),
    url(r'^like_article/(?P<id>\d+)/$', like_article, name="like_article"),
    
]
