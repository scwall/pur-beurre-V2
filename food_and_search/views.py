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
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = research_product_form(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            product_cleaned = form.cleaned_data['product']
            product = Product.objects.filter(name__icontains=product_cleaned)
            if product.exists():

                categories = Categorie.objects.filter(products__id=product[0].id)
                products = Product.objects.filter(categorie__in=categories).filter(nutrition_grade='a')
                paginator = Paginator(products, 9)
                page = request.GET.get('page', 1)
                print(page)
                products_paginator = paginator.page(page)


                context = {'products': products_paginator}
            else:
                raise Http404("Je n'ai trouvé votre produit {}".format(product_cleaned))

            return render(request,'response.html', context )




    # if a GET (or any other method) we'll create a blank form
    else:
        form = research_product_form()

    return render(request, 'index.html', {'form': form})

def signup_view(request):
    form = dict

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            print('réussi')
            return redirect('/food/')
        else:
            form = UserCreationForm()
    return render(request,'signup.html', {'form': form })

def login(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        if request.method == 'POST':
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                print(User.objects.all())
        else:
            form = AuthenticationForm()
    return  render(request,'login.html', {'form':form})

@login_required(login_url='/food/login/')
def userpage(request):

    return render(request,'userpage.html')