from django.http import HttpResponse
from django.shortcuts import render
from.models import Places
from.models import Team

# Create your views here.

def about(request):
    obj1 = Places.objects.all()
    obj2 = Team.objects.all()
    return render(request,"index.html",{'result1':obj1,'result2':obj2})



