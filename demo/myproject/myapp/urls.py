from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name="home"),
    # path('add/', views.addition, name="addition"),
    # path('add/', views.addition, name="addition"),

]
