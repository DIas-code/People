from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from .forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView
from .models import User

from main .models import Basket
from django.contrib.auth.decorators import login_required
# Create your views here.

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm()

    context = {'form': form}
    return render(request, 'users/login.html', context)

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, 'users/register.html', context)

@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(instance=request.user, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = UserProfileForm(instance=request.user)
    
    baskets = Basket.objects.filter(user=request.user)
    

    total_quantity = 0
    total_sum = 0
    for basket in baskets:
        total_quantity += basket.quantity
    for basket in baskets:
        total_sum += basket.sum()
    context = {
        "title" : "Store - Profile",
        "baskets": baskets,
        "total_sum": total_sum,
        "total_quantity": total_quantity
    }
    
    return render(request, 'users/profile.html', context)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse(''))