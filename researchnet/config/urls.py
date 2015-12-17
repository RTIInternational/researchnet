
"""researchnet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from core import views

import dashboard.views

router = routers.DefaultRouter()
router.register(r'submission', views.SubmissionViewSet)

urlpatterns = [
    url(r'^$', dashboard.views.index),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^accounts/login/$', login),
    url(r'^logout/$', logout),

]  

urlpatterns += format_suffix_patterns([
    url(r'^submission/$', views.submission_list),
    url(r'^submission/(?P<pk>[0-9]+)/$', views.submission_detail), 

])



# Needed until the static file deployment situation is figured out
urlpatterns += staticfiles_urlpatterns()




