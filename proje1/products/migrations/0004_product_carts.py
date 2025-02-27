# Generated by Django 5.0.2 on 2024-04-12 18:22

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_likes'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='carts',
            field=models.ManyToManyField(blank=True, null=True, related_name='carted', to=settings.AUTH_USER_MODEL),
        ),
    ]
