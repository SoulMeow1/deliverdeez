from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import *
from django.contrib.auth.models import Group
#from .filters import *
# Create your views here.

def home(request):
    return redirect('login')

@login_required(login_url = 'login')
@staff_only
def staffHome(request):
    delivery = Delivery.objects.all()
    pending = delivery.filter(status = 'Pending').count()

    context = {'delivery': delivery, 'pending': pending}
    return render(request, 'accounts/staffHome.html', context)

@login_required(login_url = 'login')
@allowed_users(allowed_roles=['PartTimer'])
def partTimeHome(request):
    delivery = Delivery.objects.all()
    deli = delivery.filter(status = "Pending") 

    partTimer = PartTimer.objects.get(user_id = request.user.id)

    context = {'delivery': deli, 'partTimer': partTimer}
    return render(request, 'accounts/partTimeHome.html', context)

@login_required(login_url = 'login')
def partTimeProfile(request, pk):
    pt = PartTimer.objects.get(id=pk)
    delivery = Delivery.objects.all()
    deli = delivery.filter(partTimer = pt.id)

    context = {'partTimer': pt, 'delivery': deli}
    return render(request, 'accounts/partTimeProfile.html', context)

@login_required(login_url = 'login')
def acceptDelivery(request, pk):
    deli = Delivery.objects.get(id=pk)
    partTimer = PartTimer.objects.get(user_id = request.user.id)
    if request.method == 'POST':
        deli.status = 'Out for delivery'
        deli.partTimer = partTimer
        deli.save()
        return redirect('partTimeHome')

    context = {'delivery': deli}
    return render(request, 'accounts/acceptDelivery.html', context)

@login_required(login_url = 'login')
def completeDelivery(request, pk):
    deli = Delivery.objects.get(id=pk)
    if request.method == 'POST':
        deli.status = 'Delivered'
        deli.save()
        return redirect('partTimeHome')

    context = {'delivery': deli}
    return render(request, 'accounts/completeDelivery.html', context)

@login_required(login_url = 'login')
@allowed_users(allowed_roles=['Staff'])
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
@allowed_users(allowed_roles=['Staff'])
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
@allowed_users(allowed_roles=['Staff'])
def deleteDelivery(request, pk):
    deli = Delivery.objects.get(id=pk)

    if request.method == 'POST':
        deli.delete()
        return redirect('staffHome')

    context = {'delivery': deli}
    return render(request, 'accounts/deleteDelivery.html', context)

@unauthenticated_user
def userLogin(request):

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

@unauthenticated_user
def register(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name = 'PartTimer')
            user.groups.add(group)

            messages.success(request, 'Account was created for ' + username)
            PartTimer.objects.create(user = user, name = username)
            return redirect('login')

    context = {'form': form}
    return render(request, 'accounts/register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')