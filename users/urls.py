from django.urls import path
from . import views
from .views import profile_view

urlpatterns = [
    path('profile', views.profile_view, name='profile')
]

