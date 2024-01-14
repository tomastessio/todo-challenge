from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from drf_yasg.utils import swagger_auto_schema


from .serializers import *
from .models import *

# Operaciones CRUD Básicas

# Vista de las tareas
@swagger_auto_schema(security=[{"Bearer": []}])
class TaskList(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['title','created']
    search_fields = ['title', 'description', 'created']

@swagger_auto_schema(security=[{"Bearer": []}])
class DetailTask(generics.RetrieveUpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

@swagger_auto_schema(security=[{"Bearer": []}])
class CreateTask(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

@swagger_auto_schema(security=[{"Bearer": []}])
class DeleteTask(generics.DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
