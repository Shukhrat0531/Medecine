from . import views
from django.urls import path
from . models import *

urlpatterns = [
    path('', views.index, name='index'),
    path('/about', views.about, name='about'),
    path('/about', views.naseleniya, name='naseleniya'),
    path('/news', views.news, name='news'),
    path('/press', views.press, name='press'),
    path('/zakup', views.zakup, name='zakup'),
    path('/detailist', views.detailist, name='detailist'),
   


]    
