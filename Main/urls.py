from django.urls import path

from .views import index_view, login_view, signUp_view

urlpatterns = [
    path('', index_view, name='index'),
    path('login/', login_view, name='login'),
    path('signup/', signUp_view, name='signUp'),

]
