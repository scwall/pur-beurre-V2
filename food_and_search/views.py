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
    user_products = Product.objects.filter(user_product__exact=current_user.id)
    paginator = Paginator(user_products, 6)
    page = request.GET.get('product')
    products_paginator = paginator.get_page(number=page)
    context = {'products': products_paginator}
    if request.method == 'POST':
        print('test')
        current_user = request.user
        id_product = int(request.POST['product_form'])
        product = Product.objects.get(id=id_product)
        product.user_product.remove(current_user)
        context['save_product'] = 'Produit supprimé '
        context['id_product'] = id_product

    return render(request,'userpage.html',context)

def result(request):
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
        # return render(request, 'result.html', context)
    if request.method == 'POST':
        if request.user.is_authenticated:
            print('test')
            current_user = request.user
            id_product = int(request.POST['product_form'])
            product = Product.objects.get(id=id_product)
            product.user_product.add(current_user)
            context['save_product'] = 'Produit sauvegardé'
            context['id_product'] = id_product
        else:
            return redirect('/user')

    return render(request, 'result.html', context)




