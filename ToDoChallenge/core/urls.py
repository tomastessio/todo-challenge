from django.urls import path
from .views import *

urlpatterns = [
    path('<int:pk>/', DetailTask.as_view()),
    path('', TaskList.as_view()),
    path('create', CreateTask.as_view()),
    path('delete/<int:pk>', DeleteTask.as_view()),
]
