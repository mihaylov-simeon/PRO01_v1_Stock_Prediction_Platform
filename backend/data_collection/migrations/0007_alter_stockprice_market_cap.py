# Generated by Django 5.1.2 on 2024-11-04 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_collection', '0006_remove_stockprice_cdp_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockprice',
            name='market_cap',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=35, null=True),
        ),
    ]
