from django.shortcuts import render,redirect
from .forms import studForm,updateForm
from .models import *

# Create your views here.

def index(request):
    if request.method=='POST':
        stdata=studForm(request.POST)
        if stdata.is_valid(): #true
            stdata.save()
            print("Data saved successfully!")
        else:
            print(stdata.errors)
    return render(request,'index.html')

def showdata(request):
    stdata=student.objects.all()
    return render(request,'showdata.html',{'stdata':stdata})

def update(request,id):
    stid=student.objects.get(id=id)
    if request.method=='POST':
        update=updateForm(request.POST,instance=stid)
        if update.is_valid():
            update.save()
            print("Record updated!")
            return redirect('showdata')
        else:
            print(update.errors)
    return render(request,'update.html',{'stid':stid})

def deletedata(request,id):
    stid=student.objects.get(id=id)
    student.delete(stid)
    return redirect('showdata')