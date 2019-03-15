from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='Index'),
    path('books/<slug:slug>/', views.book_detail, name='book_detail')
]
