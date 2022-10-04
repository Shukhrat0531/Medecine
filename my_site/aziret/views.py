from operator import index
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse

from .models import News, Peoples



def index(request):
    peoples =Peoples.objects.all()
    news = News.objects.all()
    return render(request,"aziret/index.html", {'peoples':peoples,'news':news})


def about(request):
    return render(request,"aziret/about.html")


def naseleniya(request):
    return render(request,"aziret/naseleniya.html")

def news(request,id):
    news = News.objects.get(id=id)
    return render(request,"aziret/news.html",{'news':news})

def press(request):
    return render(request,"aziret/press.center.html")

def zakup(request):
    return render(request,"aziret/zakup.html")

def detailist(request,pk):
    peoples =Peoples.objects.get(id=pk)

    return render(request,"aziret/detailist.html",{'peoples':peoples})



