# Generated by Django 2.2.3 on 2019-08-30 15:36

from django.db import migrations, models
import sNeeds.apps.account.models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0027_auto_20190813_0538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consultantprofile',
            name='profile_picture',
            field=models.ImageField(upload_to=sNeeds.apps.account.models.get_consultant_image_path),
        ),
        migrations.AlterField(
            model_name='consultantprofile',
            name='resume',
            field=models.FileField(blank=True, null=True, upload_to=sNeeds.apps.account.models.get_consultant_resume_path),
        ),
        migrations.AlterField(
            model_name='country',
            name='picture',
            field=models.ImageField(upload_to='images/account/country-pictures'),
        ),
        migrations.AlterField(
            model_name='fieldofstudy',
            name='picture',
            field=models.ImageField(upload_to='images/account/field-of-study-pictures'),
        ),
        migrations.AlterField(
            model_name='university',
            name='picture',
            field=models.ImageField(upload_to='images/account/university-pictures'),
        ),
    ]
