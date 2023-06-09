"""hello URL Configuration

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
from django.urls import re_path
from firstapp import views


# urlpatterns = [
#     path('', views.index),
#     re_path(r'^about', views.about),
#     re_path(r'^contact', views.contact),
#     path('products/', views.products),  # маршрут по умолчанию
#     path('products/<int:productid>/', views.products),
#     path('users/', views.users),    # маршрут по умолчанию
#     path('users/<int: id>/<str:name>/', views.users),
# ]


# urlpatterns = [
#     path('', views.index),
#     re_path(r'^about', views.about),
#     re_path(r'^contact', views.contact),
#     # path('products/',views.products), # Параметры по умолчанию
#     path('products/<int:productid>/',views.products),
#     path('users/',views.users), # Параметры по умолчанию
#     # path('users/<int:id>/<str:name>/',views.users),
#
#     # re_path(r'^products/(?P<productid>\d+)/', views.products),
#     # re_path(r'^users/(?P<id>\d+)/(?P<name>\D+)/', views.users),
#     # re_path(r'^products/$', views.products), # Параметры по умолчанию
# ]

urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('contact/', views.contact),
    path('details/', views.details),
    path('bad/', views.m400)
]
