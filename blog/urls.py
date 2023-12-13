from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('singlepost/<str:pk>', views.singlePost, name="singlepost"),

]
