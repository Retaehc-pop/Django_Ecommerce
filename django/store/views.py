from django.shortcuts import render
from rest_framework import generics

from .models import Product,Category
from .serializer  import ProductSerializer

# Create your views here.
class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class  = ProductSerializer

class Product(generics.RetrieveAPIView):
    lookup_field = "slug"
    queryset = Product.objects.all()
    serializer_class = ProductSerializer