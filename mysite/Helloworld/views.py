from django.shortcuts import render
from django.http import HttpResponse

def homePageView(request):
    return HttpResponse('CINS465 Hello World')
# Create your views here.

def hi(request):
    return render(request,'index.html',{'message':'CINS465 HELLO WORLD!'})
    #return HttpResponse('CINS465 Hello World!!!!!!!!!!!!')

def add(request):

    val1 = request.POST['num1']
    val2 = request.POST['num2']
    result = int(val1) + int(val2)

    return render(request,'result.html',{'res':result})
