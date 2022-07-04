from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('kitchen/', views.kitchen),
    path('bathroom/', views.bathroom),
    path('living/', views.living),
    path('bedroom/', views.bedroom),
    path('search/', views.search),
    path('products/', views.products),
]