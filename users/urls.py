from django.urls import path
from .views import login_view, register_view, logout_view, show_user, contact_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('show_user/', show_user, name='show_user'),
    path('contact/', contact_view, name='contact'),
]