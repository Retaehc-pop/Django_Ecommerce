from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import (
  Category,
  Product,
  ProductTypes,
  ProductSpecification,
  ProductImage,
  ProductSpecificationValue,
)

admin.site.register(Category,MPTTModelAdmin)

class ProductSpecificationInline(admin.TabularInline):
  model = ProductSpecification

@admin.register(ProductTypes)
class ProductTypeAdmin(admin.ModelAdmin):
  inlines = [ProductSpecificationInline]
# Register your models here.

class ProductImageInline(admin.TabularInline):
  model = ProductImage

class ProductSpecificationValueInline(admin.TabularInline):
  model = ProductSpecificationValue

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
  inlines = [
        ProductSpecificationValueInline,
        ProductImageInline,
    ]
  