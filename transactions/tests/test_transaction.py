import os
from rest_framework import test, status
from rest_framework.reverse import reverse 
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from ..models import Transaction
# Create your tests here.

User = get_user_model()

class TrasnactionTestCase(test.APITestCase):

   
    def setUp(self) -> None:
        super().setUp()
        os.environ.setdefault('TEST', 'True')
        self.url = reverse('transactions:transactions-list', kwargs={"version":"v1"})
        self.user = User.objects.create(username="test", email="test@test.com", password="123test456/*")
        self.refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(self.refresh.access_token))

    def test_success_transaction(self):
        data={
            "from_currency":"USD",
            "to_currency":"AED",
            "amount":10
        }
        response = self.client.post(path=self.url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_required_fields(self):
        data={
        }
        response = self.client.post(path=self.url, data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_required_fields(self):
        Transaction.objects.create(user=self.user, 
                                                 from_currency="USD", to_currency="AED",exhange_rate='0.35', 
                                                 amount="10",result="3.5")
        response = self.client.get(path=self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['count'], 1)