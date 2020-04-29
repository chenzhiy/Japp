"""ks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path,include,re_path

from django.conf.urls import url
from . import view, testdb, search, search2

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',view.hello),
    #path('hello/',view.hello),
    # re_path(r'^index/$',view.hello,name='hello'),

    url(r'^testdb$',testdb.testdb),
    url(r'^test-network$',testdb.test_network),
    url(r'^register$',testdb.register),
    url(r'^home',testdb.home),
    url(r'^register-form$',search.register_form),
    url(r'^login$', testdb.login),
    url(r'^login-form$', search.login_form),
    url(r'^search-form$',search.search_form),
    url(r'^search$',search.search),
    url(r'search-post',search2.search_post),
]
