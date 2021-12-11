from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index_chat'),
    path('<str:room_name>/', views.room, name='room'),
]