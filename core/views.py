from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from .models import *


class StockPriceView(generics.ListCreateAPIView):
    serializer_class = StockPriceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        ticker = self.request.query_params.get('ticker')
        if ticker:
            return StockPrice.objects.filter(ticker=ticker)
        return StockPrice.objects.all()


class PredictionResultView(generics.ListCreateAPIView):
    serializer_class = PredictionResultSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        stock_ticker = self.request.query_params.get('ticker')
        model_used = self.request.query_params.get('model_used')
        queryset = PredictionResult.objects.all()

        if stock_ticker:
            queryset = queryset.filter(stock__ticker=stock_ticker)
        if model_used:
            queryset = queryset.filter(model_used=model_used)
        return queryset


class AlertView(generics.ListCreateAPIView):
    serializer_class = AlertSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Alert.objects.filter(user=self.request.user)


class AlertUpdateView(generics.RetrieveDestroyAPIView):
    serializer_class = AlertSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Alert.objects.filter(user=self.request.user)


class UserProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return UserProfile.objects.filter(user=self.request.user)