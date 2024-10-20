# from django import forms
from .models import Product
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields=[
            'title',
            'content',
            'price',
            'sale_price'
        ]