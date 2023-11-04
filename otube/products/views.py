from django.shortcuts import render

from products.models import Product, ProductCategory


def index(request):
    context = {
        'title': 'OTubeProject',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all()
        }
    return render(request, 'products/index.html', context)

