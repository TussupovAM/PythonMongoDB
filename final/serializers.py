# serializers.py
from rest_framework import serializers
from .models import CustomUser
from db_connection import db


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'username', 'password',)  # Укажите поля для сериализации

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)

        # Optionally, hash the password before saving to MongoDB
        hashed_password = self.context['request'].data.get('password')
        user_data = {
            'email': user.email,
            'username': user.username,
            'password': hashed_password,  # Store hashed password in MongoDB
            # Добавьте другие поля по необходимости
        }
        db.custom_user_collection.insert_one(user_data)

        return user
