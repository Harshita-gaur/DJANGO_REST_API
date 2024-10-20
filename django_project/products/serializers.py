# from django import forms
from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Product
from api.serializers import UserPublicSerializer
from . import validators



class ProductInlineSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(
            view_name='product-detail',
            lookup_field='pk',
            read_only=True
    )
    # title = serializers.CharField(validators.validate_title_no_hello,read_only=True)
    
    
class ProductSerializer(serializers.ModelSerializer):
    # related_products= ProductInlineSerializer(source='user.product_set.all',read_only=True,many=True)
    # email=serializers.EmailField(write_only=True)
    owner=UserPublicSerializer(source='user',read_only=True)
    # my_user_data = serializers.SerializerMethodField(read_only=True)
    # my_discount = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    title = serializers.CharField(validators=[validators.validate_title_no_hello,validators.unique_product_title])
    # name = serializers.CharField(source='title',read_only=True)
    # email = serializers.EmailField(source='user.email',read_only=True)
    body=serializers.CharField(source='content')
    class Meta:
        model=Product
        fields=[
            'owner',
            # 'my_user_data',
            'user',
            'edit_url',
            'pk',
            'title',
            # 'name',
            # 'email',
            'content',
            'body',
            'price',
            'sale_price',
            'get_discount',
            # 'my_discount',
            # 'related_products',
            'path',
            'endpoint'
        ]
    def get_my_user_data(self,obj):
        return {
            "username":obj.user.username
        }  
    # def validate_title(self,value):
    #     request= self.context.get('request')
    #     user=request.user
    #     qs = Product.objects.filter(user=user,title__iexact=value)#case sensitive
    #     # qs=Product.objects.filter(title__exact=value)    
    #     if qs.exists():
    #         raise serializers.ValidationError(f"{value} is already a product name.")
    #     return value
    # def create(self,validated_data):
    #     # return Product.objects.create(**validated_data)
    #     # email=validated_data.pop('email')
    #     obj= super().create(validated_data)
    #     # print(email,obj)
    #     return obj
    
    # def update(self,instance,validated_data):
    #     email=validated_data.pop('email')
    #     return super().update(instance,validated_data)
        
    #     # instance.title=validated_data.get('title')
    #     # return instance
         
    
    def get_edit_url(self,obj):
        # return f"/api/v2/products/{obj.pk}/"
        request = self.context.get('request') 
        if request is None:
            return None
        return reverse("product-edit", kwargs={"pk": obj.pk}, request=request) 
        
    # def get_my_discount(self,obj):
        
    #     # try:
    #     # # print(obj.id)
    #     # #obj.user-->user.username
    #     #     return obj.get_discount()
    #     # except:
    #     #     return None
        
    #     if not hasattr(obj,'id'):
    #         return None
    #     if not isinstance(obj,Product):
    #         return None
    #     return obj.get_discount()
    
#you can have different serializers for the same model 

