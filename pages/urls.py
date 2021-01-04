
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, {'page': 'about'}, name='index'),
    path('<str:page>/', views.index, name='page'),
]
