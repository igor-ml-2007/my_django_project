from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    images = Image.objects.all()
    categories = Category.objects.all()
    products = Product.objects.all()[:5]
    trends = Product.objects.all().order_by('-price')[:5]
    new_products = Product.objects.all().order_by('-created_at')[:5]

    context = {
        'title': 'Main page',
        'images': images,
        'categories': categories,
        'products': products,
        'trends': trends,
        'new': new_products
    }

    return render(request, 'main.html', context)

def category_page_view(request, category_id):

    products = Product.objects.filter(category=category_id)
    context = {
        'title': f'Category: {Category.objects.get(id=category_id).title}',
        'products': products,
        'cat': Category.objects.get(id=category_id).title
    }

    return render(request, 'huy.html', context)

def category_page_view_2(request, category_id):
    products = Product.objects.filter(images_cat=category_id)
    cat = Image.objects.get(id=category_id).title
    context = {
        'title': f'Category brand: {Image.objects.get(id=category_id).title}',
        'products': products,
        'cat': cat
    }
    return render(request, 'brand.html', context)


def all_products_page(request):
    images = Image.objects.all()
    categories = Category.objects.all()
    products = Product.objects.all()

    context = {
        'title': 'Main page',
        'images': images,
        'categories': categories,
        'products': products
    }

    return render(request, 'all_products.html', context)




