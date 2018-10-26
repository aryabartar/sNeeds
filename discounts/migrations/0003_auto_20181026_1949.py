# Generated by Django 2.0.5 on 2018-10-26 16:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('discounts', '0002_auto_20181026_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdiscount',
            name='discount',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_discounts', to='discounts.Discount'),
        ),
    ]
