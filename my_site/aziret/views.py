from operator import index
from urllib import request
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse

from .models import News, Peoples

from .models import Product



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

def ecomin(request):
    return render(request,"aziret/ekozere.html")

def detailist(request,pk):
    peoples =Peoples.objects.get(id=pk)

    return render(request,"aziret/detailist.html",{'peoples':peoples})




def product_list(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'aziret/zakup.html', context)

from django.shortcuts import render, get_object_or_404
from .models import Product, Order
from .forms import OrderForm

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.product = product
            order.user = request.user
            order.save()
            return redirect('order_confirmation')
    else:
        form = OrderForm()
    context = {
        'product': product,
        'form': form,
    }
    return render(request, 'product_detail.html', context)    


from django.shortcuts import render, get_object_or_404
from .models import Product, Order
from .forms import OrderForm

def order_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.product = product
            order.user = request.user
            order.save()
            return redirect('/')
    else:
        form = OrderForm()
    context = {
        'product': product,
        'form': form,
    }
    return render(request, 'aziret/product_detail.html', context)    