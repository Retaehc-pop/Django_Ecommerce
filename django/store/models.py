from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel,TreeForeignKey


class Category(MPTTModel):
  name = models.CharField(
      verbose_name=_("Category Name"),
      help_text=_("Required and unique"),
      max_length=255,
      unique=True
   )
  slug = models.SlugField(
     verbose_name=_("Category safe URL"),
     max_length=255,
     unique=True)
  parent = TreeForeignKey("self",on_delete=models.CASCADE,null=True,blank=True,related_name="children")
  is_active = models.BooleanField(default=True)

  class MPTTMETA:
    order_insertion_by = ['name']

  class Meta:
    verbose_name = _("Category")
    verbose_name_plural = _("Categories")
  def get_absolute_url(self):
      return reverse("store:category_list", args=[self.slug])
  
  def __str__(self):
    return self.name


class ProductTypes(models.Model):
  name = models.CharField(
    verbose_name=_("Product Name"),
    help_text=_("Required"),
    max_length=255
    )
  is_active = models.BooleanField(default=True)

  class Meta:
    verbose_name = _("Product Type")
    verbose_name_plural = _("Product Types")

  def __str__(self):
    return self.name

class ProductSpecification(models.Model):
  product_tyoe = models.ForeignKey(ProductTypes,on_delete=models.RESTRICT)
  name = models.CharField(
    verbose_name=_("Product Name"),
    help_text=_("Required"),
    max_length=255
    )
  class Meta:
    verbose_name = _("Product Specification")
    verbose_name_plural = _("Product Specifications")
  def __str__(self) -> str:
      return self.name

class Product(models.Model):
  product_type = models.ForeignKey(ProductTypes,on_delete=models.RESTRICT)
  Category = models.ForeignKey(Category,on_delete=models.RESTRICT)
  title = models.CharField(
    verbose_name=_("Title"),
    help_text=_("Required"),
    max_length=255
    )
  slug = models.SlugField(max_length=255)
  description = models.TextField(verbose_name=_("Description"),help_text=_("Required"),blank=True)
  regular_price = models.DecimalField(
    verbose_name=_("Regular Price"),
    help_text=_("Required"),
    error_messages={
      "name":{
        "max_length": "The price must be between 0 - 999.99"
      }
    },
    max_digits=5,
    decimal_places=2)
  discount_price = models.DecimalField(
    verbose_name=_("Discount Price"),
    help_text=_("Required"),
    error_messages={
      "name":{
        "max_length": "The price must be between 0 - 999.99"
      }
    },
    max_digits=5,
    decimal_places=2,
    )
  is_active = models.BooleanField(
    verbose_name=_("Product visibility"),
    help_text=_("Change the visibility of the product"),
    default=True
    )
  created = models.DateTimeField(_("Created at"),auto_now_add=True,editable=False)
  updated = models.DateTimeField(_("Updated at"),auto_now=True,editable=True)
  
  class Meta:
    verbose_name = _("Product")
    verbose_name_plural = _("Products")
    ordering = ['-created']

  def __str__(self):
    return self.title
  
  def get_absolute_url(self):
    return reverse("store:product_detail", args=[self.slug])
  
class ProductSpecificationValue(models.Model):
  product = models.ForeignKey(Product,on_delete=models.CASCADE)
  specification = models.ForeignKey(ProductSpecification,on_delete=models.RESTRICT)
  value = models.CharField(
    verbose_name=_("Value"),
    help_text=_("Required"),
    max_length=255
    )

  class Meta:
    verbose_name = _("Product Specification Value")
    verbose_name_plural = _("Product Specification Values")

  def __str__(self):
      return self.value

class ProductImage(models.Model):
  product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name="product_image")
  image = models.ImageField(
    verbose_name=_("Image"),
    help_text=_("upload product image"),
    upload_to="images/",
    default="images/default.png"
  )

  alt_text = models.CharField(
    verbose_name=_("Alt Text"),
    help_text=_("add alternative text"),
    max_length=255,
    null=True,
    blank=True
  )
  is_feature = models.BooleanField(default=False)
  
  created = models.DateTimeField(_("Created at"),auto_now_add=True,editable=False)
  updated = models.DateTimeField(_("Updated at"),auto_now=True,editable=True)
  class Meta:
    verbose_name = _("Product Image")
    verbose_name_plural = _("Product Images")
  