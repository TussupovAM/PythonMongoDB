# views.py
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import CustomUser
from .serializers import UserSerializer
from db_connection import db

class UserRegistrationView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        user = serializer.instance

        # Save user data to MongoDB
        user_data = {
            'email': user.email,
            'username': user.username,
            'password': user.password,
            # Добавьте другие поля по необходимости
        }
        db.custom_user_collection.insert_one(user_data)

        return Response(serializer.data)
class UserLoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = CustomUser.objects.filter(email=email).first()

        if user and user.check_password(password):
            # Save user data to MongoDB on login (if needed)
            user_data = {
                'email': user.email,
                'username': user.username,
                # Добавьте другие поля по необходимости
            }
            db.custom_user_collection.insert_one(user_data)

            return Response({'message': 'Login successful'})
        return Response({'error': 'Invalid credentials'}, status=400)