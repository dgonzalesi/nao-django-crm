from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.

def index(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST.get("password")
        print(request.POST['username'])
        print(request.POST)
    return render(request, 'index.html', {})

def login_user(request):
    pass

def logout_user(request):
    pass
