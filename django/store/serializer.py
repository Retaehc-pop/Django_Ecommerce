from .models import Category, Product, ProductImage
from rest_framework import serializers


class ImageSerializer(serializers.ModelSerializer):
  class Meta:
    model  = ProductImage
    fields = ["image", "alt_text"]

class ProductSerializer(serializers.ModelSerializer):
  product_image = ImageSerializer(many=True, read_only=True)
  class Meta:
    model  = Product
    fields = ["id","title","description","regular_price","discount_price","product_image","slug"]

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name", "slug"]