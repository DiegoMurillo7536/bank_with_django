
from django.urls import path
from . import views

urlpatterns = [
    path('', views.bank, name='bank'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_user, name='register'),
]