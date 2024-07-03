from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LoginInfoViewSet
from .views import verify

login_router = DefaultRouter()
login_router.register('login', LoginInfoViewSet, basename='login')

# Include the router's URLs into the urlpatterns
urlpatterns = [
    path('', include(login_router.urls)),
    path('verify/', verify, name='verify')
]