from rest_framework import test, status
from rest_framework.reverse import reverse 
from django.contrib.auth import get_user_model


# Create your tests here.

User = get_user_model()

class UserCreationTestCase(test.APITestCase):

   
    def setUp(self) -> None:
        super().setUp()
        self.url = reverse('users:signup', kwargs={"version":"v1"})
       
    def test_success_signup(self):
        data={
            "username":"test",
            "email":"test@test.com",
            "first_name":"test",
            "last_name":"test",
            "password":"123test456/*"
        }
        response = self.client.post(path=self.url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_invalid_email(self):
        data={
            "username":"test",
            "email":"test@test",
            "first_name":"test",
            "last_name":"test",
            "password":"123test456/*"
        }
        response = self.client.post(path=self.url, data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_required_fileds(self):
        data={
            "email":"test@test.com",
            "first_name":"test",
            "last_name":"test",
            "password":"123test456/*"
        }
        response = self.client.post(path=self.url, data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    