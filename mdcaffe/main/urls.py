from django.urls import path
from . import views
from rest_framework import routers
from .api import IncomingMessageViewSet

router = routers.DefaultRouter()
router.register('api/incomingmessage', IncomingMessageViewSet, 'incomingmessage')

urlpatterns = [
    path('', views.index, name='home'),
    path('contacts', views.contacts, name='contacts'),
    #path('menu', views.create, name='menu'),
]