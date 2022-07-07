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
    path('my_cart/', views.my_cart),
    path('about_us/', views.about_us),
]