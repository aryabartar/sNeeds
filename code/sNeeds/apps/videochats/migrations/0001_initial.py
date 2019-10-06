# Generated by Django 2.2.3 on 2019-08-13 05:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('store', '0003_soldtimeslotsale_used'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consultant_login_url', models.URLField()),
                ('user_login_url', models.URLField()),
                ('time_slot', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='store.SoldTimeSlotSale')),
            ],
        ),
    ]
