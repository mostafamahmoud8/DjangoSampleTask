from rest_framework import viewsets, response, status, mixins
from .models import Transaction
from .serializers import TransactionSerializer
from .filters import TransactionFilter

# Create your views here.

class TransactionVewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
     
    filterset_class = TransactionFilter
 
    def get_serializer_class(self):
        return TransactionSerializer
    
    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user).order_by('-created_at')
    
    def create(self, request, *args, **kargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(serializer.data, status=status.HTTP_200_OK) 
