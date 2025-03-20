from django.urls import path,include
from . import views
urlpatterns = [
    path('signUp/', views.user_signUp,name='signUp'),
    path('login/', views.user_login,name='login'),
    path('profile/', views.user_profile,name='profile'),
    path('logout/', views.user_logout,name='logout'),
]
