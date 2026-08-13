from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def vista1(Request):
    return HttpResponse("<h1>Hola Mundo</h1>")


