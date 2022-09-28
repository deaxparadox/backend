from django.shortcuts import render
from django.views import generic

# Create your views here.

class ProgramingView(generic.TemplateView):
    template_name: str = "programming/index.html"

