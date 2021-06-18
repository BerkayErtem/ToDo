from django.urls import path
from django.conf.urls import include, url
from .views import *
urlpatterns = [
    path('', list, name='list'),
    path("add/", add, name="add"),
    path('delete/<int:id>', delete, name='delete'),
    path('active/<int:id>', active,name='active')
    
]
