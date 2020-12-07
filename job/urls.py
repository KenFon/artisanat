from django.urls import path
from . import views


urlpatterns = [
    path('jobs/<int:pk>/', views.job),
    path('jobs/', views.job),
]