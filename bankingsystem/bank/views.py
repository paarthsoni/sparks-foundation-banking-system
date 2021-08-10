from django.shortcuts import render

from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from bank.models import customer,transferhistory
from django.contrib import messages
from datetime import datetime
def index(request):
    return render(request,"index.html")

def transfer(request):
    data=customer.objects.all()
    return render(request,"transfer.html",{'objs':data})

def money(request):
     data=customer.objects.all()
     return render(request,"money.html",{'objs':data})
    
def customerinput(request,id):
    customername=customer.objects.filter(id=id)
    stu = {
     "student_number": customername
    }
    return render(request,"customerinput.html",stu)

def confirmtransfer(request):
    if request.method=="POST":
            sender=request.POST.get('sender')
            amount=request.POST.get("amount")
            security=request.POST.get("security")
            a=customer.objects.get(id=sender)
            if int(a.currentbalance) >=int(amount) and security=="281202":
                a.currentbalance=int(a.currentbalance)-int(amount)
                a.save()
                receiver=request.POST.get("receiver")
                b=customer.objects.get(id=receiver) 
                b.currentbalance=int(b.currentbalance)+int(amount)
                b.save()
                transferdetails=transferhistory.objects.create(sender=a.name,semail=a.email,receiver=b.name,remail=b.email,amount=amount)
                messages.success(request, ' Money Transfer Success!!')
                return redirect("/money")
            
            elif int(a.currentbalance) < int(amount):
                messages.warning(request, "Sorry Amount to be transferred exceeded the sender's account balance!!")
                return redirect("/transferfail")
            
            elif security!="281202":
                messages.warning(request, "Sorry Entered Security Key is Invalid!!")
                return redirect("/transferfail")
            


    return render(request,"customerinput.html")

        
def transferfail (request):
    return render(request,"transferfail.html")


def transferhistorypage(request):
    datahistory=transferhistory.objects.all()
    return render(request,"transferhistorypage.html",{'data':datahistory})



