from django.views import generic


class ProjectCounterView(generic.TemplateView):
    template_name: str = "programming/project/counter/counter_javascript.html"