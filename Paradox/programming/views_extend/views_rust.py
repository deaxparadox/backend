from django.views import generic


class RustView(generic.TemplateView):
    template_name: str = "programming/rust.html"

class RustStructureStructView(generic.TemplateView):
    template_name: str = "programming/rust/advance/structure/struct.html"

class RustStructureMethodView(generic.TemplateView):
    template_name: str = "programming/rust/advance/structure/methods.html"

class RustEnumWhatIsEnumView(generic.TemplateView):
    template_name: str = "programming/rust/enum_pattern_matching/enum.html"