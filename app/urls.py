
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, {'page': 'about'}, name='index'),
    path('contact/', views.contact, name='contact'),
    path('<str:page>/', views.index, name='page'),
]
