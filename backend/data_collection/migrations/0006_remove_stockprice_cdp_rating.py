# Generated by Django 5.1.2 on 2024-11-03 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data_collection', '0005_alter_stockprice_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stockprice',
            name='cdp_rating',
        ),
    ]
