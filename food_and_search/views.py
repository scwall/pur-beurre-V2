from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, redirect
from django.template import loader
from django.core.paginator import Paginator
from food_and_search.models import Categorie, Product
from .forms import research_product_form
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
def index(request):

    return render(request, 'index.html')

@login_required(login_url='/login/')
def save_product(request):
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

    return render(request, 'save_product.html', context)

def result(request):
    product_cleaned = str(request.GET['product'])
    if product_cleaned.isdigit() == False:
        request.session['product_session'] = product_cleaned
    product = Product.objects.filter(name__icontains=product_cleaned)
    if product.exists():
        categories = Categorie.objects.filter(products__id=product[0].id)
        products = Product.objects.filter(categorie__in=categories).order_by('nutrition_grade')
        paginator = Paginator(products, 6)
        page = request.GET.get('product')
        products_paginator = paginator.get_page(number=page)
        context = {'products': products_paginator,'original_product': Product.objects.filter(name__icontains=request.session.get('product_session'))[0]}

    else:
        raise Http404(product_cleaned)
        # return render(request, 'result_product.html', context)
    if request.method == 'POST':
        if request.user.is_authenticated:
            current_user = request.user
            id_product = int(request.POST['product_form'])
            product = Product.objects.get(id=id_product)
            product.user_product.add(current_user)
            context['save_product'] = 'Produit sauvegardé'
            context['id_product'] = id_product
        else:
            return redirect('/login')

    return render(request, 'result_product.html', context)

def detail_product(request, pk):
    product = get_object_or_404(Product,pk=pk)
    return render(request,template_name='detail_product.html',context={'detail_product':product} )


@login_required(login_url='/login/')
def user_account(request):
    return render(request,template_name='user_page.html')

