# Generated by Django 2.2.3 on 2019-09-11 07:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0028_auto_20190830_1536'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudyField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Math', 'ریاضی و فیزیک'), ('Natural Science', 'علوم تجربی'), ('Human Science', 'علوم انسانی')], max_length=16)),
            ],
        ),
        migrations.AddField(
            model_name='consultantprofile',
            name='StudyField',
            field=models.ForeignKey(blank=True, null=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='account.StudyField'),
        ),
    ]