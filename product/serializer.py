from rest_framework import serializers
from product.models import Product, Customer, Purchase

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class ListaCustomerProductSerializer(serializers.ModelSerializer):
    product = serializers.ReadOnlyField(source='product.title')
    customer = serializers.ReadOnlyField(source='customer.username')
    age = serializers.ReadOnlyField(source='customer.age')

    class Meta:
        model = Purchase
        fields = ['id', 'product', 'customer', 'age']