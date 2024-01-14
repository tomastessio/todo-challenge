from django.urls import path

from .views import *

urlpatterns = [
    path('', user_api_view, name='usuarios'),
    path('<int:pk>/', user_detail_view, name='usuarios_detail_view'),
]
