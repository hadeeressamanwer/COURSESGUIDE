from django.shortcuts import render
from django.http import HttpResponse
from .models import Languages


def index(request):
    languages=Languages.objects.all()
    return render(request,'index.html',{'languages':languages})


def new(request):
    return HttpResponse('<h1> COURSES</h1> ')



