from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from snippets.models import Snippet
from snippets.serializers import SnippetSerializers

@csrf_exempt
def snippet_list(request):
    """
    List all code snippets; or create a new snippet.
    """
    match request.method:
        
        case "POST":
            data = JSONParser().parse(request)
            serializer = SnippetSerializers(data=data)
            if serializer.is_valid():
                return JsonResponse(serializer.data, status=201)
            return JsonResponse(serializer.errors, status=400)    
        
        case default:
            snippets = Snippet.objects.all()

            """
            We can also serialize querysets instead of model instances. 
            To do so we simply add a `many=True` flag to the serializer arguments.
            """
            serializer = SnippetSerializers(snippets, many=True)
            return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def snippet_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return HttpResponse(status=404)
    
    match request.method:
        case "PUT":
            data = JSONParser().parse(request)
            serializer = SnippetSerializers(snippet, data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data)
            return JsonResponse(serializer.errors, status=400)
        
        case "DELETE":
            snippet.delete()
            return HttpResponse(status=204)

        case default:
            serializer = SnippetSerializers(snippet)
            return JsonResponse(serializer.data)
        