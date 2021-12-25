from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import CustomUser
from .serializers import CustomUserSerializer
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView



class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['email'] = user.email
        token['id'] = user.id

        # ...

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class CustomUserCreate(APIView):
    permission_classes = (permissions.AllowAny,) # why we are doing this?

    def get(self, request, format=None):
        user = CustomUser.objects.all()
        serializer = CustomUserSerializer(user, many=True)
        return Response(serializer.data)

    def post(self, request, format='json'):
        serializer = CustomUserSerializer(data=request.data) # recieving the data, but how? and in which format
        if serializer.is_valid():  # checking whether data the is valid or not, but on what basis
            user = serializer.save()  # saving the data
            if user:
                json = serializer.data  # no idea what it's doing, need to ask
                print(json)
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



