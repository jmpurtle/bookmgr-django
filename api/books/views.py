from django.contrib.auth.models import User
from rest_framework import viewsets
from .models import Book
from .serializers import UserSerializer, BookSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    resource_name = 'books'
    queryset = Book.objects.all().order_by('-title')
    serializer_class = BookSerializer