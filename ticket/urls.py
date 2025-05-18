from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('index/', views.get_index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_login, name='logout'),
    path('profile/', views.profile, name='profile'),
    # path('edit-profile/', views.edit_profile, name='edit_profile'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)