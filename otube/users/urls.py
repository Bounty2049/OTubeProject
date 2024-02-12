from django.urls import path

from users import views
from users.views import UserAPI

app_name = 'users'

urlpatterns = [
   path('login/', views.login, name='login'),
   path('registration/', views.registration, name='registration'),
   path('profile/', views.profile, name='profile'),
   path('logout/', views.logout, name='logout'),
   path('api/json-list/', views.user_list, name='user_list'),
   path('api/json-detail/<int:pk>/', views.user_detail, name='user_detail'),
   path('api/list/', UserAPI.as_view()),
   path('api/detail/<int:pk>/', UserAPI.as_view())
]