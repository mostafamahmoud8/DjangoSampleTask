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
    
    def post(self, request, *args, **kwargs):
        user_serializer = UserSerializer(data=request.data)
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save()
        return self.get_tokens_for_user(user)



