from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('stocks/', StockPriceView.as_view(), name='stocks-prices'),
    path('predictions/', PredictionResultView.as_view(), name='prediction-result'),
    path('alerts/', AlertView.as_view(), name='alerts'),
    path('alerts/<int:pk>/', AlertUpdateView.as_view(), name='alert-update'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
]
