
#this should be the first thing to do to create the link first.
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name = 'home'),
    path('count/', views.count, name = 'count'),
    path('about/', views.about, name = 'about'),  #its always a good practice to give '/' in the last of the path's first address.
]
