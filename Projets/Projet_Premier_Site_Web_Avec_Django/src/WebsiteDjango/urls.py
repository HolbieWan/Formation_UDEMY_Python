"""WebsiteDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from tkinter.font import names

from django.contrib import admin
from django.urls import path, include
from django.views.defaults import server_error

from .views import index
# from app1_blog.views import blog_index

urlpatterns = [
    path('', index, name="index"),
    path('admin/', admin.site.urls),
    path('blog/', include("app1_blog.urls"))
    # path('blog/', blog_index, name="blog_index")
]
