from rest_framework import serializers
from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Product
        fields = ('id', 'title', 'description', 'preview', 'video', 'category', 'user')

    def create(self, validated_data):
        return Product.objects.create(**validated_data)


