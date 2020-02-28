# Generated by Django 2.2.3 on 2020-02-27 05:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_auto_20200221_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='used_consultant_discount',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='discounts.ConsultantDiscount'),
        ),
    ]