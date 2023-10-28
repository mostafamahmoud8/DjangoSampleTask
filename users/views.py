from django.db import transaction
from rest_framework import views, status, response
from .serializers import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.

class UserCreateApiView(views.APIView):
    """
    user registration takes user info and return an access and refresh JSON web
    token pair to prove the authentication of those credentials.
    """
    permission_classes = []

    def get_tokens_for_user(self, user):
        refresh = RefreshToken.for_user(user)

        return response.Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_201_CREATED)
    
    @transaction.atomic()
    def post(self, request, *args, **kwargs):
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid():
           user = user_serializer.save()
           return self.get_tokens_for_user(user)
        return response.Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


