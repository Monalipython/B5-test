from django.shortcuts import redirect, render
from django.http import HttpResponse
import datetime

# Create your views here.
def fun(request):
    msg = datetime.datetime.now()
    return render('base.html',context = {'msg':msg})


    #This is for git practice
    
