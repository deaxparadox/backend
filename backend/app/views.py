from django.shortcuts import render
from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = "app/index.html"
    
    
class AppsView(TemplateView):
    template_name = "app/apps.html"