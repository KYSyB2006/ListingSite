from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginSite, name='login'),
    path('logout/', views.logoutSite, name='logout'),
]