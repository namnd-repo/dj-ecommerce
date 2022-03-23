from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

# Create your views here.

def home(request):
    return render(request, 'store/index.html')

def categories(request):
    category = Category.objects.filter(status=0)
    context = {'category':category}
    return render(request, 'store/categories.html', context)

def categoriesview(request, slug):
    if (Category.objects.filter(slug=slug, status=0)):
        products = Product.objects.filter(category__slug=slug)
        category = Category.objects.filter(slug=slug).first()
        context = {'products': products, 'category': category}
        return render(request, 'store/products/index.html', context)
    else:
        messages.warning(request, "No such category found")
        return redirect('categories')

def productview(request, cate_slug, prod_slug):
    if (Category.objects.filter(slug=cate_slug, status=0)):
        if (Product.objects.filter(slug=prod_slug, status=0)):
            products = Product.objects.filter(slug=prod_slug, status=0).first
            context = {'products':products}
        else:
            messages.error(request, "No such category found")
            return redirect('categories')
    else:
        messages.error(request, "No such category found")
        return redirect('categories')
    return render(request, 'store/products/view.html', context)