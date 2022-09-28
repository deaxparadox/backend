from django.views import generic

class JavascriptView(generic.TemplateView):
    template_name: str = "programming/javascript.html"