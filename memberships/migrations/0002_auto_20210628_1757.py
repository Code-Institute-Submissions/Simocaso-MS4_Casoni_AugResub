# Generated by Django 3.2.4 on 2021-06-28 17:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('memberships', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='membership',
            options={'verbose_name_plural': 'Memberships'},
        ),
        migrations.RemoveField(
            model_name='membership',
            name='sku',
        ),
    ]
