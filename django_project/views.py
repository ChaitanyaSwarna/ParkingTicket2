from django.shortcuts import render, redirect
from django_project import models,forms
from datetime import datetime
from .forms import DetailsForm, PastForm
from django.views import View
from django_project.models import Region, Input

regions=list(Region.objects.all())

class Home(View):
  def get(self, request):
    return render(request,"index.html",{"form":DetailsForm()})

  def post(self, request):
    a_date=datetime.strptime(request.POST['time'], "%Y-%m-%dT%H:%M")
    a_day=a_date.strftime("%A")
    
    a_copy=request.POST.copy()
    a_copy.update({'day':a_day})
    form=DetailsForm(a_copy)
    
    if form.is_valid():
      form.save()
    return render(request,'index.html',{'regions':regions,'form':DetailsForm()})
    # else:
    #   return render(request,"index.html",{"form":form})

class History(View):
  def get(self,request):
    return render(request,"history.html",{'form':PastForm()})

  def post(self, request):
    region=request.POST["region"]
    day=request.POST["day"]
    a_list=list(Region.objects.filter(name=region))[0]
    pasttickets=Input.objects.filter(region=a_list,day=day)
    print("Pasttickets",pasttickets)
    return render(request,'history.html',{"regions":list(regions),"pasttickets":list(pasttickets),"form":PastForm()})
    
      
    
    
    

