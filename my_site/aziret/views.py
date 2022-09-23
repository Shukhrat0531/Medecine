from operator import index
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse



def index(request):
    return render(request,"aziret/index.html")


def about(request):
    return render(request,"aziret/about.html")


def naseleniya(request):
    return render(request,"aziret/naseleniya.html")

def news(request):
    return render(request,"aziret/news.html")

def press(request):
    return render(request,"aziret/press.center.html")

def zakup(request):
    return render(request,"aziret/zakup.html")

def detailist(request):
    return render(request,"aziret/detailist.html")



