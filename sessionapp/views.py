from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,'home.html')
def add(request):
    x=int(request.POST["t1"])
    y=int(request.POST["t2"])
    z=x+y
    request.session["res"]=z
    request.session.set_expiry(100)
    resp=HttpResponse("data submitted successfully")
    return resp
def display(request):
    if request.session.has_key("res"):
        s=request.session["res"]
        return HttpResponse("the sum is:"+str(s))
    else:
        return render(request,'home.html')