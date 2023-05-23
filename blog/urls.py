from . import views
from django.urls import path

urlpatterns = [
    path('', views.Homepage, name='blog-home'),
    path('about/', views.about, name='blog-about'),
]