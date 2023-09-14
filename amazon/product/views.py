from django.shortcuts import render
from . models import *

def home(request):
    d = {
        'data': user.objects.all(),

    }
    return render(request,'home.html',d)

def about(request):
    c={
        'data':pro.objects.all(),
    }
    return render(request,'about.html',c)

def contact(request):
    return render(request,'contact.html')

