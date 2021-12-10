from django.shortcuts import render
from rest_framework import viewsets, permissions
from api.serializers import TodoSerializer
from api.models import Todo

# Class Model Viewset
class TodoModelViewSet(viewsets.ModelViewSet):
    # Define the serializer class
    serializer_class = TodoSerializer
    # Define the queryset
    queryset = Todo.objects.all()

    # Permissions (left to your own exercise)
    # permission_classes = [permissions.IsAuthenticated]

    # Define the list of allowed HTTP methods (by default if you didn't define it, it will just enable all)
    http_method_names = ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']

