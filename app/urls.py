
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, {'page': 'about'}, name='index'),
    path('email/', views.email_test, name='email-test'),
    path('<str:page>/', views.index, name='page'),
]
