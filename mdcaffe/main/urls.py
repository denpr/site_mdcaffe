from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('contacts', views.contacts, name='contacts'),
    #path('menu', views.create, name='menu'),
]