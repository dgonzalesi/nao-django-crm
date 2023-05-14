from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Record
# Create your views here.

def index(request):
    records = Record.objects.all()

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
        print(records[0])
        return render(request, 'index.html', { 'records': records })

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
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("La cuenta fue creada con el nombre de usuario: " + username))
            return redirect('index')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})

    return render(request, 'register.html', {'form': form})


def customer_record(request, pk):
    print(pk)
    if request.user.is_authenticated:
        # Look up record
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record': customer_record})
    else:
        messages.success(request, ("Debes estar autenticado para ver esta pagina"))
        return redirect('index')
