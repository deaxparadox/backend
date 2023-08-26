"""
## Wrapping API views

REST framework provides two wrappers you can use to write API views.

- The `@api_view` decorator for working with function based views.
- The `APIView` class for working with class-based views.
"""


from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from snippets.models import Snippet
from snippets.serializers import SnippetSerializers

@api_view(["GET", "POST"])
def snippet_list(request):
    """
    List all code snippets, or create a new snippet.
    """

    if request.method == "GET":
        snippets = Snippet.objects.all()
        serializer = SnippetSerializers(snippets, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = SnippetSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(["GET", "PUT", "DELETE"])
def snippet_detail(request, pk):
    """
    Retreive, update and delete a code snippet.
    """
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = SnippetSerializers(snippet)
        return Response(serializer.data)
    
    elif request.method == "PUT":
        serializer = SnippetSerializers(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == "DELETE":
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)