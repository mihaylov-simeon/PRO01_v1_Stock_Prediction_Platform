from django.shortcuts import render
from rest_framework import generics, status
from .serializers import StockPriceSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from .models import StockPrice

def index(request):
    return render(request, 'data_collection/index.html')

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
