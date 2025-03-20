from django.urls import path,include
from . import views
urlpatterns = [
    path('signUp/', views.user_signUp,name='signUp'),
]
