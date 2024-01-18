from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Product
        fields = ('id', 'title', 'description', 'preview', 'video', 'category', 'user')