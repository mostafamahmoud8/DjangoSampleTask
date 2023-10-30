from rest_framework import test, status
from rest_framework.reverse import reverse 
from django.contrib.auth import get_user_model


# Create your tests here.

User = get_user_model()

class UserLoginTestCase(test.APITestCase):

   
    def setUp(self) -> None:
        super().setUp()
        self.url = reverse('users:token_obtain_pair', kwargs={"version":"v1"})
        self.username = "test"
        self.password = "123test456/*"
        user = User.objects.create(username=self.username)
        user.set_password(self.password)
        user.save()


    def test_success_login(self):
        data={
            "username": self.username,
            "password": self.password
        }
        response = self.client.post(path=self.url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_fail_login(self):
        data={
            "username":self.username,
            "password":"wrongpassword"
        }
        response = self.client.post(path=self.url, data=data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        