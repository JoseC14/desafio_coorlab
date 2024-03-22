from rest_framework import serializers


class TransportSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=150)
    price_confort = serializers.CharField(max_length=9)
    price_econ = serializers.CharField(max_length=9)
    city = serializers.CharField(max_length=150)
    duration = serializers.CharField(max_length=3)
    seat = serializers.CharField(max_length=3)
    bed = serializers.CharField(max_length=2)
    
        