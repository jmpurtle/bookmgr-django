from django.contrib.auth.models import User, Group
from .models import Book
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('url', 'username', 'email', 'groups')

class BookSerializer(serializers.ModelSerializer):
	class Meta:
		model = Book
		fields = '__all__'