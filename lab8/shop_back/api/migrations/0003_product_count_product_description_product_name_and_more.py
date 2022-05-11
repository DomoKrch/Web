# Generated by Django 4.0.4 on 2022-04-12 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_category_name_product_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='product',
            name='name',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.FloatField(default=0),
        ),
    ]