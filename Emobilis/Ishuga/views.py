from django.shortcuts import render
from django.http import HttpResponse
from . models import Student, Teacher, School
# Create your views here.


def index(request):
    return render(request, 'index.html')

def students(request):
    student = Student.objects.all()
    return render(request, 'students.html', {"student":student})

def teacher(request):
    teacher = Teacher.objects.all()
    return render(request, 'teachers.html', {"teacher":teacher})

def school(request):
    school = School.objects.all()
    return render(request, 'school.html', {"school":school})

def insert_students(request):
    return render(request, 'insert_students.html')