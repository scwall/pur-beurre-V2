from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, redirect
from django.template import loader
from django.core.paginator import Paginator
from food_and_search.models import Categorie, Product
from .forms import research_product_form

def index(request):

    return render(request, 'index.html')

@login_required(login_url='/accounts/login/')
def userpage(request):
    current_user = request.user

    product2 = Product.objects.filter(user_product__exact=current_user.id)
    context = {'products':product2}
    return render(request,'userpage.html',context)

def result(request):
    paginator = object
    if request.method == 'GET':
        product_cleaned = request.GET['product']
        product = Product.objects.filter(name__icontains=product_cleaned)
        if product.exists():
            categories = Categorie.objects.filter(products__id=product[0].id)
            products = Product.objects.filter(categorie__in=categories).order_by('nutrition_grade')
            paginator = Paginator(products, 6)
            page = request.GET.get('product')
            products_paginator = paginator.get_page(number=page)
            context = {'products': products_paginator}
        else:
            raise Http404(product_cleaned)
        return render(request, 'result.html', context)


    else:
        raise Http404(' aucun produit chargé')





