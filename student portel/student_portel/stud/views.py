from django.shortcuts import render
from . models import *
# Create your views here.

db=student.objects.all()

def index(request):
    if request.method=="POST":
        username= request.POST['username']
        password= request.POST['password']
        try:
            use= student.objects.get(username=username, password=password)
            
            return render(request,'success.html', {'username': username,"db":use})
        except student.DoesNotExist:
            return render(request, 'index.html', {'error': 'Invalid username or password'})
    return render(request,'index.html')