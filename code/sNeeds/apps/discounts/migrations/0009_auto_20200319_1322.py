# Generated by Django 2.2.3 on 2020-03-19 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20200308_0756'),
        ('discounts', '0008_discount_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='discount',
            name='products',
            field=models.ManyToManyField(blank=True, to='store.Product'),
        ),
    ]
