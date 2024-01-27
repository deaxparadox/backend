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

# class HeadingDetailModelSerializer(serializers.ModelField)