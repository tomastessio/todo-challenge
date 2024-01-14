from rest_framework.test import APITestCase
from rest_framework import status

from faker import Faker

faker = Faker()

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
    

    def test_dasdasd(self):
        print(self.token)

