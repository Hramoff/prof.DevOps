from . import views
from django.urls import path

urlpatterns = [
    path('', views.index),
    path('register/', views.register),
    path('authorized/', views.authorized)
]
