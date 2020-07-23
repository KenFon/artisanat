from django.urls import path
from . import views


urlpatterns = [
    path('profiles/<int:pk>/', views.profile),
    path('profiles/', views.profiles),
]