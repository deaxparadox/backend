from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token

from asyncio import sleep as asleep
from time import sleep

from pms.api.helpers.auth import get_token_from_header

from ..serializers import HeadingModelSerializer
from ..serializers.single_heading import (
    heading_HeadingSerializer_single_task, 
    heading_TaskSerializer_single_task,
)
from pms.models.heading import Heading


@api_view(["GET"])
def home_view(request):
    """
    Home View
    
    Get all headings.
    """
    # sleep(3)
    # user_token: str | None = get_token_from_header(request)
    
    # if not user_token:
    #     return Response({}, status=status.HTTP_401_UNAUTHORIZED)
    
      
    # headings = user_token.user.heading.all()
    headings = Heading.objects.all().order_by("-created")
    
    serializers = HeadingModelSerializer(headings, many=True)
    return Response(
        serializers.data,
        status=status.HTTP_200_OK
    )
    



class HeadingDetail(APIView):
    # filterset_fields = ['category', 'in_stock']

    def get(self, request, id):
        # id = self.kwargs['id']                                # for query parameter
        # user_token = get_token_from_header(request)
        
        # try:
        #     heading = user_token.user.heading.get(id=id)
        # except Heading.DoesNotExist:
        #     return Response({}, status=status.HTTP_404_NOT_FOUND)
        
        heading = Heading.objects.get(id=id)
        
        # serializers = heading_HeadingSerializer_single_task(heading)
        serializers = HeadingModelSerializer(heading)
        
        return Response(
            serializers.data,
            status=status.HTTP_200_OK
        )
        
        
@api_view(["POST"])
def create_heading(request):
    user_token: str | None = get_token_from_header(request)
    if not user_token:
        return Response({}, status=status.HTTP_401_UNAUTHORIZED)
    
    # get `heading` data from request
    heading = request.data.get("heading")
    
    # create new `Heading` object
    new_heading = user_token.user.heading.create(heading=heading)
    
    # serializer the heading
    serializer = HeadingModelSerializer(new_heading)
    
    # return a response
    return Response(serializer.data, status=status.HTTP_201_CREATED)