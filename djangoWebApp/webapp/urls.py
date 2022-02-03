from django.conf import settings
from django.template.defaulttags import url
from django.urls import path, include
from django.views.static import serve

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.gallery, name='gallery'),
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
