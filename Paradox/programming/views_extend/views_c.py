from django.views import generic

class CView(generic.TemplateView):
    template_name: str = "programming/c.html"