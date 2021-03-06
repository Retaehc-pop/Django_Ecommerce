# Generated by Django 4.0.3 on 2022-04-04 06:52

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Required and unique', max_length=255, unique=True, verbose_name='Category Name')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Category safe URL')),
                ('is_active', models.BooleanField(default=True)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='store.category')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Required', max_length=255, verbose_name='Title')),
                ('slug', models.SlugField(max_length=255)),
                ('description', models.TextField(blank=True, help_text='Required', verbose_name='Description')),
                ('regular_price', models.DecimalField(decimal_places=2, error_messages={'name': {'max_length': 'The price must be between 0 - 999.99'}}, help_text='Required', max_digits=5, verbose_name='Regular Price')),
                ('discount_price', models.DecimalField(decimal_places=2, error_messages={'name': {'max_length': 'The price must be between 0 - 999.99'}}, help_text='Required', max_digits=5, verbose_name='Discount Price')),
                ('is_active', models.BooleanField(default=True, help_text='Change the visibility of the product', verbose_name='Product visibility')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='store.category')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='ProductSpecification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Required', max_length=255, verbose_name='Product Name')),
            ],
            options={
                'verbose_name': 'Product Specification',
                'verbose_name_plural': 'Product Specifications',
            },
        ),
        migrations.CreateModel(
            name='ProductTypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Required', max_length=255, verbose_name='Product Name')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Product Type',
                'verbose_name_plural': 'Product Types',
            },
        ),
        migrations.CreateModel(
            name='ProductSpecificationValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(help_text='Required', max_length=255, verbose_name='Value')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product')),
                ('specification', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='store.productspecification')),
            ],
            options={
                'verbose_name': 'Product Specification Value',
                'verbose_name_plural': 'Product Specification Values',
            },
        ),
        migrations.AddField(
            model_name='productspecification',
            name='product_tyoe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='store.producttypes'),
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='images/default.png', help_text='upload product image', upload_to='images/', verbose_name='Image')),
                ('alt_text', models.CharField(blank=True, help_text='add alternative text', max_length=255, null=True, verbose_name='Alt Text')),
                ('is_feature', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_image', to='store.product')),
            ],
            options={
                'verbose_name': 'Product Image',
                'verbose_name_plural': 'Product Images',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='product_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='store.producttypes'),
        ),
    ]
