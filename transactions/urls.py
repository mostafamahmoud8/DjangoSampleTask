from rest_framework import routers
from .views import TransactionVewSet

app_name = "transactions"

router = routers.DefaultRouter()
router.register(r'transaction', TransactionVewSet, basename='transactions')

urlpatterns = router.urls