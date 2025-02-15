# Generated by Django 4.2 on 2024-11-25 21:48

import core.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Alert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alert_type', models.CharField(choices=[('price', 'Price Alert'), ('volume', 'Volume Alert')], max_length=50)),
                ('target_price', models.DecimalField(decimal_places=2, max_digits=10, validators=[core.models.Alert.validate_positive_price])),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('threshold_type', models.CharField(choices=[('above', 'Above'), ('below', 'Below')], default='above', max_length=10)),
                ('expiration_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='HistoricalPrediction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prediction_date', models.DateTimeField(auto_now=True)),
                ('prediction_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('actual_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('model_used', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='HistoricalPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticker', models.CharField(max_length=10)),
                ('date', models.DateTimeField()),
                ('open', models.DecimalField(decimal_places=2, max_digits=10)),
                ('high', models.DecimalField(decimal_places=2, max_digits=10)),
                ('low', models.DecimalField(decimal_places=2, max_digits=10)),
                ('close', models.DecimalField(decimal_places=2, max_digits=10)),
                ('volume', models.BigIntegerField()),
                ('market_cap', models.DecimalField(blank=True, decimal_places=2, max_digits=35, null=True)),
                ('pe_ratio', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('high_52_week', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('low_52_week', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PredictionResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prediction_date', models.DateTimeField()),
                ('prediction_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('actual_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('model_used', models.CharField(max_length=100)),
                ('confidence_score', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_notifications', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='StockPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticker', models.CharField(max_length=10)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('open', models.DecimalField(decimal_places=2, max_digits=10)),
                ('high', models.DecimalField(decimal_places=2, max_digits=10)),
                ('low', models.DecimalField(decimal_places=2, max_digits=10)),
                ('close', models.DecimalField(decimal_places=2, max_digits=10)),
                ('volume', models.BigIntegerField()),
                ('market_cap', models.DecimalField(blank=True, decimal_places=2, max_digits=35, null=True)),
                ('pe_ratio', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('high_52_week', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('low_52_week', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_picture', models.ImageField(blank=True, height_field=30, null=True, upload_to='', width_field=30)),
                ('notifications', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddIndex(
            model_name='stockprice',
            index=models.Index(fields=['ticker', 'date'], name='core_stockp_ticker_b9a792_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='stockprice',
            unique_together={('ticker', 'date')},
        ),
        migrations.AddField(
            model_name='settings',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='predictionresult',
            name='stock',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.stockprice'),
        ),
        migrations.AddField(
            model_name='predictionresult',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddIndex(
            model_name='historicalprice',
            index=models.Index(fields=['ticker', 'date'], name='core_histor_ticker_d18f44_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='historicalprice',
            unique_together={('ticker', 'date')},
        ),
        migrations.AddField(
            model_name='historicalprediction',
            name='stock',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.stockprice'),
        ),
        migrations.AddField(
            model_name='alert',
            name='stock',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.stockprice'),
        ),
        migrations.AddField(
            model_name='alert',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='predictionresult',
            unique_together={('stock', 'prediction_date')},
        ),
    ]
