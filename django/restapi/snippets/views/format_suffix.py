"""
# Adding optional format suffixes to our URLs

```py
def snippet_list(request, format=None):
```

and 


```py
def snippet_detail(request, pk, format=None):
```

Now update the `snippets/urls.py` file slightly, to append 
a set of `format_suffix_patterns` in addition to the existing URLs.

```py
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [
    path('snippets/', views.snippet_list),
    path('snippets/<int:pk>/', views.snippet_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
```



### We can control the format of the response that we get back, 
either by using the `Accept` header

```bash
http http://127.0.0.1:8000/snippets/ Accept:application/json  # Request JSON
http http://127.0.0.1:8000/snippets/ Accept:text/html         # Request HTML
```

Or by appending a format suffix:

```bash
http http://127.0.0.1:8000/snippets.json  # JSON suffix
http http://127.0.0.1:8000/snippets.api   # Browsable API suffix
```

"""

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from snippets.models import Snippet
from snippets.serializers import SnippetSerializers

@api_view(["GET", "POST"])
def snippet_list(request, format=None):
    """
    List all code snippets, or create a new snippet.
    """

    print(format)

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
def snippet_detail(request, pk, format=None):
    print(format)
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
    

