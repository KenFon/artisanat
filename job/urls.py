from django.urls import path
from . import views


urlpatterns = [
    path('job/<int:pk>/', views.job),
    path('jobs/', views.jobs),
]