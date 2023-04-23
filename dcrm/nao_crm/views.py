from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request, 'index.html', {})

def test(request):
    return render(request, 'test.html', {})
