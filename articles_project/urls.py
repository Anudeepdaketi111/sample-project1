
from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from django.http import HttpResponse

urlpatterns = [
   
    url(r'^', include('posts.urls')),

]
