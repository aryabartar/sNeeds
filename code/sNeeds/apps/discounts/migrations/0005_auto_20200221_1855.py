# Generated by Django 2.2.3 on 2020-02-21 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discounts', '0004_auto_20200220_0847'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timeslotsalenumberdiscount',
            name='id',
        ),
        migrations.AlterField(
            model_name='timeslotsalenumberdiscount',
            name='number',
            field=models.PositiveIntegerField(primary_key=True, serialize=False),
        ),
    ]
