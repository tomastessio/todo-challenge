from rest_framework.test import APITestCase
from rest_framework import status
from core.models import Task

from faker import Faker

faker = Faker()


## Setup para obtener el token
class TestSetUp(APITestCase):
    
    def setUp(self):
        from users.models import User

        self.login_url = '/login/'
        self.user = User.objects.create_superuser(
            name='Developer',
            last_name='Developer',
            username=faker.name(),
            password='developer',
            email=faker.email()
        )

        response = self.client.post(
            self.login_url,
            {
                'username': self.user.username,
                'password': 'developer'
            },
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.token = response.data['token']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        return super().setUp()


## Factory para crear una nueva tarea
class TaskFactory:

    def build_task_JSON(self):
        return {
            'title': 'Crear tarea desde tests',
            'description': 'Descripción random',
            'created': '2024-01-12',
            'completed': False
        }

    def create_task(self):
        return Task.objects.create(**self.build_task_JSON())


## Test para obtener la tarea creada
class TaskListTestCase(TestSetUp):

    def test_task_list(self):
        task = TaskFactory().create_task()
        response = self.client.get(
            '/api/',
            {
                'title': task.title
            },
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], task.title)

## Test para buscar una tarea que no existe, debe venir una lista vacia []
    def test_task_list_error(self):
        task = TaskFactory().create_task()
        response = self.client.get(
            '/api/',
            {
                'title': 'Tarea cualquiera'
            },
            format='json'
        )
        self.assertEqual(response.data, [])
