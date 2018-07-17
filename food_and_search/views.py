from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.urls import reverse

from food_and_search.models import Categorie, Product, SignUpForm


def index(request):
    return render(request, 'index.html')


@login_required(login_url='/login/')
def save_product(request):
    page = 0
    current_user = request.user
    user_products = Product.objects.filter(user_product__exact=current_user.id)
    paginator = Paginator(user_products, 6)
    if request.method == 'GET':
        page = request.GET.get('product')
    products_paginator = paginator.get_page(number=page)
    context = {'products': products_paginator}
    if request.method == 'POST':
        current_user = request.user
        id_product = request.POST.get('product_form')
        product = Product.objects.get(id=id_product)
        product.user_product.remove(current_user)

    return render(request, 'save_product.html', context)


def result(request):
    if request.method == 'GET':
        name_product_search = request.GET.get('product')
        save_product = request.GET.get('product-save')
        if save_product is not None:
            save_product = int(save_product)
        if name_product_search is None:
            raise Http404('Aucun produit demandé !')
        else:
            product = Product.objects.filter(name__icontains=name_product_search)

            if product.exists():
                original_product = products__id = product[0]
                categories = Categorie.objects.filter(products__id=product[0].id)
                products = Product.objects.filter(categorie__in=categories).order_by('nutrition_grade')
                paginator = Paginator(products, 6)
                page = request.GET.get('product')
                products_paginator = paginator.get_page(number=page)
                context = {'products': products_paginator, 'name_product_search': name_product_search,
                           'original_product': original_product, 'id_product': save_product}

            else:
                raise Http404(
                    "le produit {product} n'existe pas dans la base de données".format(product=name_product_search))
        return render(request, 'result_product.html', context)
    if request.method == 'POST':
        context = {}
        if request.user.is_authenticated:
            current_user = request.user
            id_product = request.POST.get('product_form')
            name_product_search = request.POST['name_product_search']
            product = Product.objects.get(id=id_product)
            product.user_product.add(current_user)
            context['id_product'] = int(id_product)
        else:
            return redirect('/login')

        return redirect(
            reverse('food_and_search:result') + '?product={name_product}&product-save={product_save}'.format(
                product_save=id_product, name_product=name_product_search))


def detail_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, template_name='detail_product.html', context={'detail_product': product})


@login_required(login_url='/login/')
def user_account(request):
    return render(request, template_name='user_page.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user_tmp = form.save()
            user_tmp.save()
            tmp_username = form.cleaned_data.get('username')
            print(tmp_username)
            tmp_password = form.cleaned_data.get('password1')
            print(tmp_password)
            user = authenticate(username=tmp_username, password=tmp_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
