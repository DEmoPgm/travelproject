from . import views
from django.urls import path

urlpatterns=[
    path('register',views.register,name='register'),
    path('loginpg',views.loginpg,name='loginpg'),
    path('logout',views.logout,name='logout'),


]