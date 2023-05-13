from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.

def index(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            messages.success(request, ("You have been logged in!"))
            return redirect('index')
        else:
            messages.success(request, "Error logging in - please try again...")
            print(messages)
            return redirect('index')
    else:
        return render(request, 'index.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out!")
    return redirect('index')

def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.clean_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("La cuenta fue creada con el nombre de usuario: " + username))
            return redirect('index')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {})

