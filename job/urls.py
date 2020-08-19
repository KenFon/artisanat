from django.urls import path, include
from rest_framework.routers import DefaultRouter
from job import views

router = DefaultRouter()
router.register('job',views.JobViewSet)

urlpatterns = [
    path('',include(router.urls))
]