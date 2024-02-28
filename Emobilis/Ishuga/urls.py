from django.urls import path
from . import views

urlpatterns = [

    path('', views.index),
    path('students/', views.students),
    path('teacher/', views.teacher),
    path('school/', views.school),
    path('insert_students/', views.insert_students)


]