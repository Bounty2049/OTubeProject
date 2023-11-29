from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from products.models import Product, ProductCategory, Library
from users.models import User
from products.forms import UserCreatingLesson
from django.urls import reverse


def index(request):
    context = {
        'title': 'OTubeProject',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all()
        }
    return render(request, 'products/index.html', context)


def create(request):
    if request.method == 'POST':
        form = UserCreatingLesson(data=request.POST)
        if form.is_valid():
            title = request.POST['title']
            description = request.POST['description']
            preview = request.POST['preview']
            video = request.POST['video']
            category = ProductCategory.objects.get(id=request.POST['category'])
            new_lesson = Product(title=title, description=description, image=preview, video_url=video, category=category)
            new_lesson.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = UserCreatingLesson()

    context = {
        'title': 'Create Lesson',
        'form': form
    }

    return render(request, 'products/create.html', context)

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