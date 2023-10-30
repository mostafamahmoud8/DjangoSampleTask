from rest_framework import test, status
from rest_framework.reverse import reverse 
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

# Create your tests here.

User = get_user_model()

class UserRefreshTestCase(test.APITestCase):

   
    def setUp(self) -> None:
        super().setUp()
        self.url = reverse('users:token_refresh',kwargs={"version":"v1"})
        self.user = User.objects.create(username="test", email="test@test.com", password="123test456/*")
        self.refresh = RefreshToken.for_user(self.user)

    def test_success_refresh(self):
        data={
            "refresh":str(self.refresh),
        }
        response = self.client.post(path=self.url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)