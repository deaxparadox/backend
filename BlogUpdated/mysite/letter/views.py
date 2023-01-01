from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator

from .Front.HTML.a import a

from .models import Letter

def LetterDetailView(request, **kwargs):
    # print(kwargs.get('slug'))
    # letter = get_object_or_404(Letter, slug=kwargs.get('slug'), status=Letter.Status.PENDING)
    letter = Letter.objects.filter(slug=kwargs.get('slug')).get()
    return render(request, "letter/post/detail.html", {
        "letter": letter
    })

def LetterListView(request):
    letters = Letter.objects.all()
    paginator = Paginator(letters, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "letter/post/list.html", {
        # "letters": letters
        "page_obj": page_obj
    })

style = """{
    background-color: black;
    color: blue;
    }
"""
def LetterTestView(request):
    return HttpResponse(a("test", Class="container", Style=style))