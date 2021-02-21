from django.contrib import admin
from django.urls import path, include
from .views import login

app_name = 'accounts'
urlpatterns = [
    path('login/', login, name='login')
]
