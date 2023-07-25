from . import views
from django.urls import path

urlpatterns = [
    path('', views.demo, name='demo'),
    path('formpg/',views.formpg,name='formpg'),

    path('add/',views.result,name='result'),

    path('passvalue/',views.passvalue,name='passvalue'),
    path('home/',views.home,name='home')




]
