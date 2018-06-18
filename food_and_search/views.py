from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.template import loader

from food_and_search.forms import research_product_form


def index(request):
    # if this is a POST request we need to process the form data
    paginator = object
    if request.method == 'GET':
        # create a form instance and populate it with data from the request:
        form = research_product_form(request.GET or None)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            product_cleaned = form.cleaned_data['product']
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
            return render(request,'response.html', context )

    else:
        form = research_product_form(request.GET or None)

    return render(request, 'index.html', {'form': form})