from django.urls import path
from . import views

urlpatterns = [

    path('', views.home),
    path('about/', views.about),
    path('contact/', views.contact),
    path('register/', views.register),
    path('role/', views.role),
    path('students/', views.students)


]