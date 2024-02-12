from django.urls import path, include

from rest_framework import routers

from products import views

app_name = 'products'

router = routers.SimpleRouter()
router.register(r'product', views.ProductViewSet)

urlpatterns = [
   path('', views.index, name='products'),
   path('category/<int:category_id>/', views.index, name='category'),
   path('libraries/add/<int:product_id>/', views.add_to_library, name='add_to_library'),
   path('libraries/delete/<int:library_id>/', views.delete_library, name='delete_library'),
   path('create/', views.create, name='create'),
   path('api/', include(router.urls)),
   path('api/list/', views.ProductViewSet.as_view({'get': 'list'})),
   path('api/update/<int:pk>/', views.ProductViewSet.as_view({'put': 'update'}))
]


'''
   path('api/v2/', include(router.urls)),  # routers
   path('api/v1/product_list/', ProductViewSet.as_view({'get': 'list'})),
   path('api/v1/product_list/<int:pk>/', ProductViewSet.as_view({'put': 'update'})),
'''