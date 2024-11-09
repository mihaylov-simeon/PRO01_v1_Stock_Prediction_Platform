from rest_framework import serializers
from .models import StockPrice

class StockPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockPrice
        fields = "__all__"

    def create(self, validate_data):
        print(validate_data)
        user = User.objects.create_user(**validate_data)
        return user