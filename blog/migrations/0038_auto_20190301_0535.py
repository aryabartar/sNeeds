# Generated by Django 2.1.3 on 2019-03-01 05:35

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0037_post_post_main_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_main_image',
            field=models.ImageField(null=True, upload_to=blog.models.upload_post_image),
        ),
    ]