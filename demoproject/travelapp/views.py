from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.








from .models import Place, Team


def demo(request):
    obj=Place.objects.all()
    tobj=Team.objects.all()
    return  render(request,"index.html",{'result':obj,'tresult':tobj})
def passvalue(request):
    name="INDIA"
    return render(request,"pvalue.html",{'obj':name})
def formpg(request):
    return render(request,"formpg.html")
def result(request):
    x=int(request.GET['num1'])
    y=int(request.GET['num2'])
    res=x+y
    return render(request,"result.html",{'result':res})
def home(request):
    return render(request,"home.html")
