from django.urls import path

from products.views import index, add_to_library, delete_library, create

app_name = 'products'

urlpatterns = [
   path('', index, name='products'),
   path('libraries/add/<int:product_id>/', add_to_library, name='add_to_library'),
   path('libraries/delete/<int:library_id>/', delete_library, name='delete_library'),
   path('create', create, name='create')
]