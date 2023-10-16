from django.shortcuts import render
from . models import *
from . forms import *
# Create your views here.
def index(request):
      db=bas_db.objects.all()
      form=bas_form()
      if request.method=='POST':
            if 'submit' in request.POST:
                  form=bas_form(request.POST)
                  form.save()
            elif 'delete' in request.POST:
                  key=request.POST.get('delete')
                  form=bas_db.objects.get(id=key)
                  form.delete()



      context={}
      context["db"]=db
      context["form"]=form



      return render(request,'index.html',context)