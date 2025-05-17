from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def profile_view(request):
    return render(request, 'ticket/profile.html')

# Create your views here.
