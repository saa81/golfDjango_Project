from django.shortcuts import render

def get_index(request):
    return render(request, 'ticket/index.html')