from django.urls import path
from . import views

app_name = 'bank'

urlpatterns = [
    path('', views.bank, name='index'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_user, name='register'),
    path('activate_account/<int:account_id>/', views.go_to_activate_account, name='go_to_activate_account'),
    path('make_transaction/', views.make_transaction, name='make_transaction'),
    path('top_account/<int:account_id>/', views.top_account, name='top_account'),
]