from email import message
from mailbox import Message
from urllib import request
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
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
    if request.user.is_authenticated:
        # Look up record
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record': customer_record})
    else:
        messages.success(request, ("Debes estar autenticado para ver esta pagina"))
        return redirect('index')

def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "El contacto ha sido borrado")
        return redirect('index')
    else:
        menssage = "Necesitas estar autentificado para llevar a cabo esa acción"
        messages.success(request, menssage)
        return render(request, 'register.html', {})
    
def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "Record Added...")
                return redirect('index')
        return render(request, 'add_record.html', {'form':form})
    else:
        messages.success(request, "Necesitas una cuenta para registrar contactos.")
        return redirect('index')