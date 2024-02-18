from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    return redirect('login')

@login_required(login_url = 'login')
def staffHome(request):
    delivery = Delivery.objects.all()
    pending = delivery.filter(status = 'Pending').count()

    context = {'delivery': delivery, 'pending': pending}
    return render(request, 'accounts/staffHome.html', context)

# @login_required(login_url = 'login')
def partTimeHome(request):
    delivery = Delivery.objects.all()
    deli = delivery.filter(status = "Pending")

    context = {'delivery': deli,}
    return render(request, 'accounts/partTimeHome.html', context)

@login_required(login_url = 'login')
def partTimeProfile(request, pk):
    pt = PartTimer.objects.get(id=pk)
    delivery = Delivery.objects.all()
    deli = delivery.filter(partTimer = pt.id)

    context = {'partTimer': pt, 'delivery': deli}
    return render(request, 'accounts/partTimeProfile.html', context)

@login_required(login_url = 'login')
def createDelivery(request):
    form = DeliveryForm()

    if request.method == 'POST':
        form = DeliveryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('staffHome')

    context = {'form': form}
    return render(request, 'accounts/createDelivery.html', context)

@login_required(login_url = 'login')
def updateDelivery(request, pk):
    deli = Delivery.objects.get(id=pk)
    form = DeliveryForm(instance=deli)

    if request.method == 'POST':
        form = DeliveryForm(request.POST, instance=deli)
        if form.is_valid():
            form.save()
            return redirect('staffHome')

    context = {'form': form}
    return render(request, 'accounts/createDelivery.html', context)

@login_required(login_url = 'login')
def deleteDelivery(request, pk):
    deli = Delivery.objects.get(id=pk)

    if request.method == 'POST':
        deli.delete()
        return redirect('staffHome')

    context = {'delivery': deli}
    return render(request, 'accounts/deleteDelivery.html', context)

def userLogin(request):
    if request.user.is_authenticated:
        return redirect('staffHome')

    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username = username, password = password)

            if user is not None:
                login(request, user)
                return redirect('staffHome')
            
            else:
                messages.info(request, 'Username or password is incorrect')


    context = {}
    return render(request, 'accounts/login.html', context)

def register(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account waas created for ' + user)
            return redirect('login')

    context = {'form': form}
    return render(request, 'accounts/register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')