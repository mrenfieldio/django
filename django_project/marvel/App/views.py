from django.shortcuts import render
from . models import *
from . forms import *
# Create your views here.
def index(request):
    db=bas_db.objects.all()
    form=bas_form()

    if request.method=='POST':
            if 'submit' in request.POST:
                  key=request.POST.get('submit')
                  if not key:
                    form=bas_form(request.POST)
                  else:
                    form_obj=bas_db.objects.get(id=key)
                    form=bas_form(request.POST,instance=form_obj)
                  form.save()
                  form=bas_form()

            elif 'delete' in request.POST:
                  key=request.POST.get('delete')
                  form=bas_db.objects.get(id=key)
                  form.delete()

                  
            elif 'edit' in request.POST:
                  key=request.POST.get('edit')
                  form_obj=bas_db.objects.get(id=key)
                  form=bas_form(instance=form_obj)
                  
                  



    context={}
    context["db"]=db
    context["form"]=form



    return render(request,'index.html',context)