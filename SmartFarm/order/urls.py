from .views import create_order, home,testmon,contact,shop,login,why
from django.contrib import admin
from django.urls import path

urlpatterns = [
    # Other URL patterns for your app
    path('', home, name='home'),
    path('why', why, name='why'),
    path('login', login, name='login'),
    path('contact', contact, name='contact'),
    path('testmon', testmon, name='testmon'),
    path('shop', shop, name='shop'),
    path('order/create/', create_order, name='create_order'),
]