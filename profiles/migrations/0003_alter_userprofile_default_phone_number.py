# Generated by Django 3.2.4 on 2021-08-12 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20210808_0934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='default_phone_number',
            field=models.CharField(blank=True, max_length=18, null=True),
        ),
    ]
