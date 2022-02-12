from django.shortcuts import render
import requests
from django.http import HttpResponse
# Create your views here.
def hi(request):
    return render(request, 'WEBAPP/hi.html')

def hello(request):
    return render(request, 'WEBAPP/hello.html')

def how(request):
    return render(request, 'WEBAPP/how.html')

def are(request):
    return render(request, 'WEBAPP/are.html')

