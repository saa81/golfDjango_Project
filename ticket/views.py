
from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

def get_index(request):
    return render(request, 'ticket/index.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = RegisterForm()
    return render(request, template_name="ticket/register.html", context={'form':form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile')
    else:
        form = AuthenticationForm
    return render(request, template_name='ticket/login.html', context={'form':form})

@login_required
def profile(request):
    return render(request, 'ticket/profile.html')

@login_required
def logout(reguest):
    return render(reguest, 'ticket/logout.html')
# Create your views here.
