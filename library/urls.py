from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('new/', views.book_new, name='book_new'),
    path('delete/<int:pk>', views.book_delete, name='book_delete'),
]