# Generated by Django 2.2.3 on 2020-03-18 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discounts', '0005_auto_20200318_2014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discount',
            name='consultants',
            field=models.ManyToManyField(blank=True, to='consultants.ConsultantProfile'),
        ),
    ]
