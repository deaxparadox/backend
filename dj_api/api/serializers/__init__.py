from rest_framework import serializers

from app.models import Person


class PersonSerializerID(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    first_name = serializers.CharField()
    last_name = serializers.CharField()

class PersonSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()

    def create(self, validated_data):
        print(validated_data)
        person = Person.objects.create(**validated_data)
        print(person)
        return person
    
    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        print(instance)
        print(validated_data)

        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.save()
        return instance