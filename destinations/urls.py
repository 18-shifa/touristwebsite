from django.urls import path
from . import views

urlpatterns = [
    path('', views.destination_list, name='destination_list'),
    path('destination/<int:pk>/', views.destination_detail, name='destination_detail'),
    path('destination/new/', views.destination_create, name='destination_create'),
    path('destination/<int:pk>/edit/', views.destination_update, name='destination_update'),
    path('destination/<int:pk>/delete/', views.destination_delete, name='destination_delete'),
]
