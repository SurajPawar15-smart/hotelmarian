"""advance URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from crud import views
from django.conf.urls import url

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$', views.index),
    #url(r'^index/$', views.index,name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^blog/$', views.blog, name='blog'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^elements/$', views.elements, name='elements'),
    url(r'^main/$', views.main , name='main'),
    url(r'^rooms/$', views.rooms , name='rooms'),
    url(r'^services/$', views.services, name='services'),
    url(r'^single_blog/$', views.single_blog, name='single_blog'),
    
]
