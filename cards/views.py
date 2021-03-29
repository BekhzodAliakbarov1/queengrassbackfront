from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *

from .models import Product

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		
		}

	return Response(api_urls)

#First Model apis
@api_view(['GET'])
def ProductList(request):
	productCards = Product.objects.all().order_by('-id')
	serializer = ProductSerializer(productCards, many=True)
	return Response(serializer.data)

@api_view(['GET']) 
def EachProductList(request, name):
	productCards = Product.objects.all().filter(typeOfProduct=name)
	serializer = ProductSerializer(productCards, many=True)
	return Response(serializer.data)

@api_view(['GET']) 
def EachProductListItemDetail(request, name, pk):
	productCards = Product.objects.all().filter(typeOfProduct=name).filter(id=pk)
	serializer = ProductSerializer(productCards, many=True)
	return Response(serializer.data)
