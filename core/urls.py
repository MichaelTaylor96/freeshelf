from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='Index'),
    path('<slug:slug>/', views.book_detail, name='Book_detail')
]
