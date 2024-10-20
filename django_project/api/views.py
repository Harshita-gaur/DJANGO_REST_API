from urllib import response
from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
import json
from products.models import Product
from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.serializers import ProductSerializer
# Create your views here.
@api_view(['POST'])
def api_home(request, *args, **kwargs):
    """
    DRF API View
    """
    data=request.data
    # if request.method !='POSt':
    #     return Response({"detail":"method not allowed"},status=400)
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        instance = serializer.save()
    #     # instance = form.save()
        print(serializer.data)
        return Response(serializer.data)
    return Response({"invalid": "not good data"}, status=400)

    # model_data= Product.objects.all().order_by("?").first() # makes a random quesry field and returns the first value
    # data={}
    # if model_data:
        # data['id']=model_data.id
        # data['title']=model_data.title
        # data['content']=model_data.content
        # data['price']=model_data.price
        # to get same exact response
        # data=model_to_dict(model_data)
    #     data=dict(data)
    #     json_data_str = json.dumps(data)
        # data=model_to_dict(model_data, fields=['id','title','price','sale_price'])
    # return HttpResponse(json_data_str, headers={"content-type":"application/json"})
    
    
    # request--> HTTP request--> django
    # print(dir(request))
    # print(request.GET) #get url query parameters
    # body=request.body  #byte string of json data
    # data={}
    # try: # try block in case there is no data in body
    #     data=json.loads(body) # takes a string of Json data --> Python dictionary
    # except:
    #     pass
    # print(data.keys())  #prints :dict_keys([]) in the terminal
    # # print(body)
    # data['params']=dict(request.GET)
    
    # data['headers']=dict(request.headers)
    # data['content_type']=request.content_type
    # return JsonResponse({"message":"Hi there,this is ur django API Response"})
    # return JsonResponse(data)
    # return Response(data)
    
    instance=Product.objects.all().order_by("?").first()
    data={}
    if instance:
        data=ProductSerializer(instance).data
    return Response(data)

