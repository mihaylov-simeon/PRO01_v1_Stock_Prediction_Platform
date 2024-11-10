from django.contrib import admin
from .models import StockPrice, PredictionResult, Alert, UserProfile, HistoricalPrediction, Settings, HistoricalPrice

admin.site.register(StockPrice)
admin.site.register(HistoricalPrice)
admin.site.register(PredictionResult)
admin.site.register(Alert)
admin.site.register(UserProfile)
admin.site.register(HistoricalPrediction)
admin.site.register(Settings)