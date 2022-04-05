from django.shortcuts import render
from rest_framework import generics
from .import models
from .models import Product,Category
from .serializer  import ProductSerializer,CategorySerializer

# Create your views here.
class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class  = ProductSerializer

class Product(generics.RetrieveAPIView):
    lookup_field = "slug"
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CategoryItemView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return models.Product.objects.filter(
            Category__in=Category.objects.get(slug=self.kwargs["slug"]).get_descendants(include_self=True)
        )

class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer