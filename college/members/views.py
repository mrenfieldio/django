from django.shortcuts import render
from . models import *
from . forms import *
# Create your views here.
def index(request):
    # db=student.objects.all()
    # db1=teacher.objects.all()
    # db2=batch.objects.all()
    # form=bas_form()
    if request.method=='POST':
        form=bas_form(request.POST)
        if form.is_valid():
         batch_filter=form.cleaned_data['name']
         print(batch_filter)
         stu=student.objects.filter(year=batch_filter)
         print('output is ',stu)
    else:
        form=bas_form()
        stu=[]

        
       

    

    context={}
    # context["db"]=db
    # context["db1"]=db1
    context["stu"]=stu
    context["form"]=form
    # print(form)

    return render(request,'index.html',context)