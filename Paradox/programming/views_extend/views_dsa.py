from django.views import generic

class DSALinkedListStackView(generic.TemplateView):
    template_name: str = "programming/dsa/linked_list/stack/stack.html"