from django.shortcuts import render
from .models import *
from . forms import *
# Create your views here.
def index(request):
    db=TASK.objects.all()
    form=Bas_form(request.POST)
   
    context={}
    context["db"]=db
    context["form"]=form
    return render(request,'index.html',context)

def create(request):
    db=TASK.objects.all()
    form=Bas_form()
    if request.method=='POST':
        bs_frm=Bas_form(request.POST)
        if bs_frm.is_valid():
           bs_frm.save()
           Bas_form()
           return index(request)
    context={}
    context["db"]=db
    context["form"]=form

    return render(request,'create.html',context)

def edit(request,p):
    data=TASK.objects.get(pk=p)
    if request.POST:
        frm=Bas_form(request.POST,instance=data)
        if frm.is_valid():
            frm.save()
            return index(request)
    else:
        frm=Bas_form(instance=data)

    return render(request,'edit.html',{"form":frm})


def delete_itm(request,p):
    key=TASK.objects.get(pk=p)
    key.delete()
    return index(request)
    
   