from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def home(request):
    return HttpResponse("Welcome to my home page")

def store(request):
    return HttpResponse("Get the best quality")

def contact(request):
    return HttpResponse("Find us using these social media platforms")

def about(request):
    return HttpResponse("Lorem ipsum dolor sit amet, consectetur adipisicing elit. <b>A ad adipisci aliquam assumenda autem,</b> <br>consectetur enim in libero nobis officia <b>pariatur sit suscipit</b> ut vel vitae.</br> Aliquid perferendis perspiciatis quod."
                        "")



