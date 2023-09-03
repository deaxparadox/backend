from rest_framework import serializers


class Add:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Add: {self.x}, {self.y}"

    def __repr__(self):
        return f"Add: {self.x}, {self.y}"


class AddSerializer(serializers.Serializer):
    x = serializers.IntegerField()
    y = serializers.IntegerField()
