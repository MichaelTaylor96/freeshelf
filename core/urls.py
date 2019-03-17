from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='Index'),
    path('<slug:slug>/', views.book_detail, name='Book_detail'),
    path('<slug:slug>/favorite/', views.favorite, name='Favorite'),
    path('<str:username>/favorites/', views.favorites, name='Favorites')
]
