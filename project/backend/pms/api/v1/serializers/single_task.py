from rest_framework import serializers

class task_HeadingSerializer_single_task(serializers.Serializer):
    id = serializers.IntegerField()
    heading = serializers.CharField()
    start = serializers.DateField(required=False)
    end = serializers.DateField(required=False)
    created = serializers.DateTimeField()
    updated = serializers.DateTimeField()

class task_TaskSerializers_single_task(serializers.Serializer):
    id = serializers.IntegerField()
    task = serializers.CharField()
    start = serializers.DateField(required=False)
    end = serializers.DateField(required=False)
    created = serializers.DateTimeField()
    updated = serializers.DateTimeField()
    heading = task_HeadingSerializer_single_task()