# Generated by Django 2.1.3 on 2019-03-01 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0036_remove_post_post_main_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_main_image',
            field=models.URLField(null=True),
        ),
    ]