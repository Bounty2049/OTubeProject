"""
URL configuration for otube project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from products.views import index
from products.views import ProductViewSet

from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'product', ProductViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('products/', include('products.urls', namespace='products')),
    path('users/', include('users.urls', namespace='users')),
    path('api/v2/', include(router.urls)),
    path('api/v2/drf-auth/', include('rest_framework.urls'))
    # path('api/v1/productlist/', ProductViewSet.as_view({'get': 'list'})),
    # path('api/v1/productlist/<int:pk>/', ProductViewSet.as_view({'put': 'update'})),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
