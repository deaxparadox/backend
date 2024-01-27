from rest_framework import serializers

from pms.models.heading import Heading
from pms.models.task import Task

# 
# Model Serializers
# 
class HeadingModelSerializer(serializers.ModelSerializer):
    """
    By default include all the fields for exporting
    """
    class Meta:
        model = Heading
        fields = "__all__"

class TaskModelSerializer(serializers.ModelSerializer):
    # heading = HeadingModelSerializer()
    class Meta:
        model = Task
        fields = "__all__"




# 
# Relational Model Serializers
# 
class TaskModel_Serializers_2(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"

class HeadingModelSerializers_2(serializers.ModelSerializer):
    tasks = TaskModel_Serializers_2(many=True)
    class Meta:
        model = Heading
        fields = "__all__"


