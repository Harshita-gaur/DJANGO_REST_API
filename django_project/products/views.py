from rest_framework import authentication,generics, mixins,permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from django.http import Http404
from django.shortcuts import get_object_or_404
# from api.authentication import TokenAuthentication
from api.mixins import (StaffEditorPermissionMixin,UserQuerySetMixin)
from .models import Product
# from ..api.permissions import IsStaffEditorPermission
from .serializers import ProductSerializer

class ProductDetailAPIView(
    StaffEditorPermissionMixin,
    generics.RetrieveAPIView):
    queryset= Product.objects.all()
    serializer_class=ProductSerializer
product_detail_view = ProductDetailAPIView.as_view()

# class ProductCreateAPIView(generics.CreateAPIView):
#     queryset= Product.objects.all()
#     serializer_class=ProductSerializer
#     permission_classes=[permissions.IsAdminUser,IsStaffEditorPermission]
#      #lookup_field ='pk'
#     #Product.objects.get(pk='abc')
#     def perform_create(self,serializer):
#         #serializer.save(user=self.request.save)
#         print(serializer.validated_data)
#         title=serializer.validated_data.get('title')
#         content=serializer.validated_data.get('content')
#         # or None
#         if content is None:
#             content=title
#         serializer.save(content=content)
# product_create_view = ProductCreateAPIView.as_view()

# class ProductListAPIView(generics.ListAPIView):
#     '''
#     not gonna use this method
#     '''
#     queryset= Product.objects.all()
#     serializer_class=ProductSerializer
    
# product_list_view = ProductListAPIView.as_view()

class ProductListCreateAPIView(
    UserQuerySetMixin,
    StaffEditorPermissionMixin,
    generics.ListCreateAPIView):
    queryset= Product.objects.all()
    serializer_class=ProductSerializer
    # allow_staff_view=False
    # user_field='owner'
    def perform_create(self,serializer):
        #serializer.save(user=self.request.save)
        # email=serializer.validated_data.pop('email')
        # print(email)
        print(serializer.validated_data)
        title=serializer.validated_data.get('title')
        content=serializer.validated_data.get('content')
        # or None
        if content is None:
            content=title
        serializer.save(user=self.request.user,content=content)  #similar to form.save() or model.save()
        
    # def get_quesryset(self, *args, **kwargs):
    #     qs=super().get_quesryset(*args, **kwargs)
    #     request=self.request
    #     user=request.user
    #     if not user.is_authenticated:
    #         return Product.objects.none()
    #     # print(request.user)
    #     return qs.filter(user=request.user)
        
product_list_create_view = ProductListCreateAPIView.as_view()

@api_view(['GET','POST'])
def product_alt_view(request,pk=None, *args, **kwargs):
    method=request.method
    
    if method == "GET":
        if pk is not None:
            #detail view
            obj =get_object_or_404(Product,pk=pk)
            data =ProductSerializer(obj,many=False).data
            return Response(data)
        # #list view
        queryset =Product.objects.all()
        data = ProductSerializer(queryset,many=True).data
        return Response(data)
            
    if method == "POST":
        #create an item
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # instance = serializer.save()
            # instance = form.save()
            title=serializer.validated_data.get('title')
            content=serializer.validated_data.get('content') or None
            if content is None:
                content=title
            serializer.save(content=content)
        return Response(serializer.data)
    return Response({"invalid": "not good data"}, status=400)


class ProductUpdateAPIView(
    StaffEditorPermissionMixin,
    generics.UpdateAPIView):
    queryset= Product.objects.all()
    serializer_class=ProductSerializer
    lookup_field='pk'
    def perform_update(self,serializer):
        instance=serializer.save()
        if not instance.content:
            instance.content=instance.title
        
        
product_update_view = ProductUpdateAPIView.as_view()

class ProductDestroyAPIView(
    StaffEditorPermissionMixin,
    generics.DestroyAPIView):
    queryset= Product.objects.all()
    serializer_class=ProductSerializer
    lookup_field='pk'
    def perform_destro(self,instance):
        super().perform_destroy(instance)
        
        
product_destroy_view = ProductDestroyAPIView.as_view()

class ProductMixinView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    generics.GenericAPIView):
    queryset= Product.objects.all()
    serializer_class=ProductSerializer
    lookup_field='pk'
    def get(self,request, *args, **kwargs):
        pk=kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request, args, **kwargs) 
        return self.list(request, args, **kwargs)
    
    def post(self,request, *args, **kwargs):
        return self.list(request, args, **kwargs)
    def perform_create(self,serializer):
        #serializer.save(user=self.request.save)
        print(serializer.validated_data)
        title=serializer.validated_data.get('title')
        content=serializer.validated_data.get('content') or None
        if content is None:
            content="single view doing cool stuff"
        serializer.save(content=content)
product_mixin_view=ProductMixinView.as_view()