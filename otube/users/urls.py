from django.urls import path

from users import views

app_name = 'users'

urlpatterns = [
   path('login/', views.login, name='login'), # without drf
   path('registration/', views.registration, name='registration'), # without drf
   path('profile/', views.profile, name='profile'), # without drf
   path('logout/', views.logout, name='logout'), # without drf
   path('api/', views.UserList.as_view()),
]