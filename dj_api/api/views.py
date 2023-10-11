from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from django.http import JsonResponse


from app.models import Person
from .serializers import PersonSerializer, PersonSerializerID

@api_view(["GET", "POST"])
def person_all_view(request):
    match request.method:
        case "GET": 
            persons = Person.objects.all()
            person_serializer = PersonSerializerID(persons, many=True)
            return  Response(person_serializer.data, status=status.HTTP_200_OK)
        case "POST": 
            data = JSONParser().parse(request)
            serializer = PersonSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        case _:
            return JsonResponse(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        
@api_view(["GET", "PUT", "DELETE"])
def person_one_view(request, id=None):
    person = None

    try:
        person = Person.objects.get(id=id)
    except Person.DoesNotExist as e:
        return JsonResponse({}, status=status.HTTP_404_NOT_FOUND)
        

    if request.method == "GET":
        try:
            person = Person.objects.get(id=id)
        except Person.DoesNotExist as e:
            return JsonResponse({}, status=status.HTTP_404_NOT_FOUND)
        serializer = PersonSerializer(person)
        return  JsonResponse(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == "PUT":
        data = JSONParser().parse(request)
        print(data)
        serializer = PersonSerializer(person, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_202_ACCEPTED)
        return  JsonResponse(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == "DELETE":
        person.delete()
        return JsonResponse(person, status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)