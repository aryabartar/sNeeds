# Generated by Django 2.0.5 on 2018-10-17 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0023_auto_20181008_2029'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserUploadedBooklet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='عنوان')),
                ('field', models.CharField(max_length=120, verbose_name='رشته')),
                ('topic', models.CharField(max_length=120, verbose_name='درس')),
                ('writer', models.CharField(max_length=120, verbose_name='نویسنده')),
            ],
        ),
    ]
