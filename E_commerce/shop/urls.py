from django.urls import path
from . import views

urlpatterns = [

    path('', views.home),
    path('store/', views.store),
    path('contact/', views.contact),
    path('about/', views.about)

]