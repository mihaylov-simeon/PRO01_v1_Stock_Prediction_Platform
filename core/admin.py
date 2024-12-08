from django.contrib import admin
from .models import (
    StockPrice,
    HistoricalPrice,
    PredictionResult,
    Alert,
    UserProfile,
    HistoricalPrediction,
    Settings,
)

@admin.register(StockPrice)
class StockPriceAdmin(admin.ModelAdmin):
    list_display = ('ticker', 'date', 'close', 'volume')
    list_filter = ('ticker', 'date')

@admin.register(HistoricalPrice)
class HistoricalPriceAdmin(admin.ModelAdmin):
    list_display = ('ticker', 'date', 'close', 'volume')
    list_filter = ('ticker', 'date')

@admin.register(PredictionResult)
class PredictionResultAdmin(admin.ModelAdmin):
    list_display = ('stock', 'prediction_date', 'prediction_price', 'actual_price', 'model_used')
    list_filter = ('model_used', 'prediction_date')
    search_fields = ('stock__ticker', 'model_used')

@admin.register(Alert)
class AlertAdmin(admin.ModelAdmin):
    list_display = ('stock', 'user', 'alert_type', 'target_price', 'is_active', 'expiration_date')
    list_filter = ('alert_type', 'threshold_type', 'is_active')
    search_fields = ('stock__ticker', 'user__username')

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'notifications')
    search_fields = ('user__username',)

@admin.register(HistoricalPrediction)
class HistoricalPredictionAdmin(admin.ModelAdmin):
    list_display = ('stock', 'prediction_date', 'prediction_price', 'actual_price', 'model_used')
    list_filter = ('prediction_date',)
    search_fields = ('stock__ticker', 'model_used')

@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ('user', 'email_notifications')