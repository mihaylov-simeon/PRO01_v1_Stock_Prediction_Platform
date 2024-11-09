from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.utils import timezone
import re

User = get_user_model()

def email_validator(value):
    email_regex = r"^[a-zA-Z0-9.!#$%&’*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$"
    if not re.match(email_regex, value):
        raise ValidationError("Invalid email address!")


class StockPrice(models.Model):
    ticker = models.CharField(max_length=10)
    date = models.DateTimeField(default=timezone.now)
    open = models.DecimalField(max_digits=10, decimal_places=2)
    high = models.DecimalField(max_digits=10, decimal_places=2)
    low = models.DecimalField(max_digits=10, decimal_places=2)
    close = models.DecimalField(max_digits=10, decimal_places=2)
    volume = models.BigIntegerField()
    market_cap = models.DecimalField(max_digits=35, decimal_places=2, null=True, blank=True)
    pe_ratio = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    high_52_week = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    low_52_week = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.ticker} - {self.date}"
    
    class Meta:
        unique_together = ['ticker', 'date']
        indexes = [
            models.Index(fields=['ticker', 'date'])
        ]


class PredictionResult(models.Model):
    stock = models.ForeignKey(StockPrice, on_delete=models.CASCADE)
    prediction_date = models.DateTimeField()
    prediction_price = models.DecimalField(max_digits=10, decimal_places=2)
    actual_price = models.DecimalField(max_digits=10, decimal_places=2)
    model_used = models.CharField(max_length=100)
    confidence_score = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # Allow null for now

    def __str__(self):
        return f"{self.stock} is predicted to be {self.prediction_price} on {self.prediction_date}"
    
    class Meta:
        unique_together = ['stock', 'prediction_date']


class Alert(models.Model):
    ALERT_TYPE_CHOICES = [
        ("price", "Price Alert"),
        ("volume", "Volume Alert")
    ]

    def positive_value(value):
        if value <= 0:
            raise ValidationError("The target price must be a positive number!")

    stock = models.ForeignKey(StockPrice, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    alert_type = models.CharField(max_length=50, choices=ALERT_TYPE_CHOICES)
    target_price = models.DecimalField(max_digits=10, decimal_places=2, validators=[positive_value])
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    threshold_type = models.CharField(max_length=10, choices=[('above', 'Above'), ('below', 'Below')], default="above")
    expiration_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.user} - {self.stock} with target price {self.target_price}"

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(height_field=30, width_field=30, null=True, blank=True)  # Optional field
    notifications = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user} - {self.profile_picture}"

class HistoricalPrediction(models.Model):
    stock = models.ForeignKey(StockPrice, on_delete=models.CASCADE)
    prediction_date = models.DateTimeField(auto_now=True)
    prediction_price = models.DecimalField(max_digits=10, decimal_places=2)
    actual_price = models.DecimalField(max_digits=10, decimal_places=2)
    model_used = models.CharField(max_length=10)

    def __str__(self):
        return f"Stock: {self.stock} - Date: {self.prediction_date}, Price: {self.prediction_price}, Actual Price: {self.actual_price}"

class Settings(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_notifications = models.BooleanField(default=True)