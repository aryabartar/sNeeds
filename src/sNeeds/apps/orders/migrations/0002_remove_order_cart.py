# Generated by Django 2.2.3 on 2020-02-21 05:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='cart',
        ),
    ]