from django.shortcuts import render
from django.http import HttpResponse
from . models import Student
# Create your views here.


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def register(request):
    return render(request, 'register.html')

def role(request):
    return render(request, 'role.html')

def students(request):
    student = Student.objects.all()
    return render(request, 'students.html', {"student":student})