from django.urls import path
from .views import index_view, signup_view, success_view

urlpatterns = [
    path('', index_view, name='index'),
    path('success/', success_view, name='success-signup'),
    path('signup/', signup_view, name='signup'),
]
