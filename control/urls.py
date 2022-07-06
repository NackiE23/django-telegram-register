from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('profile/<int:user_pk>/', profile, name='profile'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('api/v1/create_user/', UserAPICreate.as_view(), name='create_user_api'),
]
