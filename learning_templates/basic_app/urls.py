from django.urls import path
from . import views

# Template tagging

urlpatterns = [
    path('', views.relative, name='relative'),
    path('other/', views.other, name='other'),
]
