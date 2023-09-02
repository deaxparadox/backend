from rest_framework import serializers


class AddSerializer(serializers.Serializer):
    x = serializers.IntegerField(read_only=True)
    y = serializers.IntegerField(read_only=True)
