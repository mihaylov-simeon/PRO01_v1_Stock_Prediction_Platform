from django.shortcuts import render
from rest_framework import generics
from .serializers import StockPriceSerializer, UserSerializer, HistoryPriceSerializer
from rest_framework.permissions import AllowAny
from .models import StockPrice
from data_collection.models import StockPrice, HistoricalPrice
from django.contrib.auth.models import User

# def index(request):
#     return render(request, 'data_collection/index.html')

class StockPriceView(generics.ListCreateAPIView):
    serializer_class = StockPriceSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return StockPrice.objects.all()
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)


class HistoricalPriceView(generics.ListCreateAPIView):
    serializer_class = HistoryPriceSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return HistoricalPrice.objects.all()
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)

class UserRegistrationView(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return User.objects.all()
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.error)

