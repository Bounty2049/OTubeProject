from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from products.models import Product, ProductCategory, Library
from users.models import User
from products.forms import UserCreationLesson
from django.urls import reverse
from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from products.serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


    @action(methods=['get'], detail=False)
    def category(self, request):
        cats = ProductCategory.objects.all()
        return Response({'categories': [cat.title for cat in cats]})


def index(request, category_id=None):
    if category_id:
        products = Product.objects.filter(category_id=category_id)
    else:
        products = Product.objects.all()

    context = {
        'title': 'OTubeProject',
        'products': products,
        'categories': ProductCategory.objects.all()
        }
    return render(request, 'products/index.html', context)


def create(request):
    if request.method == 'POST':
        form = UserCreationLesson(data=request.POST, files=request.FILES)
        if form.is_valid():
            try:
                form.save()
                return HttpResponseRedirect(reverse('index'))
            except:
                print(None, 'ERROR')
            finally:
                print('Work with form done')
    else:
        form = UserCreationLesson()


    context = {
        'title': 'Create Lesson',
        'form': form
    }

    return render(request, 'products/create.html', context=context)


@login_required
def add_to_library(request, product_id):
    product = Product.objects.get(id=product_id)
    libraries = Library.objects.filter(user=request.user, product=product)

    if not libraries.exists():
        Library.objects.create(user=request.user, product=product)
    else:
        print('Already in library')

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def delete_library(request, library_id):
    library = Library.objects.get(id=library_id)
    library.delete()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])