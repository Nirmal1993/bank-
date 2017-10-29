from django.conf.urls import url
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^$',views.Transact.home),
    url(r'viewpage',views.Transact.show_page),
    url(r'Home',views.Transact.home),
    url(r'register',views.Transact.register),
    url(r'transaction',views.Transact.transaction),
    url(r'Deposit',views.Transact.deposit),
]
