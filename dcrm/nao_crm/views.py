from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.

def index(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST["password"]
        print(username)
    return render(request, 'index.html', {})

def login_user(request):
    pass

def logout_user(request):
    pass
