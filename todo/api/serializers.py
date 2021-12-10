from api.models import Todo
from rest_framework import serializers

class TodoSerializer(serializers.ModelSerializer):
    """
    Serializer for Todo model
    """
    class Meta:
        model = Todo
        # All fields
        fields = '__all__'