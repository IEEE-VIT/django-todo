from django.urls import path
from .views import index_view, signup_view

urlpatterns = [
    path('', index_view, name='index'),
    path('signup/', signup_view, name='signup'),
]
