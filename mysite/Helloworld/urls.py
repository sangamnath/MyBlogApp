from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePageView, name='home'),
    path('index/', views.hi, name='hi'),
    path('index/add/',views.add,name='add'),

]