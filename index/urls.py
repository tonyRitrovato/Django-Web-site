from django.urls import path
from . import views

urlpatterns = [
    path('form', views.form, name='form'),
    path('', views.index, name='index')
]