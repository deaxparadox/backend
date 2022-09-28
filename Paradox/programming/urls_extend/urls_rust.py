from django.urls import path 

from ..views_extend import views_rust

urlpatterns = [
    path("rust/", views_rust.RustView.as_view(), name="programming_rust"),
    path("rust/structure/struct/", views_rust.RustStructureStructView.as_view(), name="programming_rust_structure_struct"),
    path("rust/structure/methods/", views_rust.RustStructureMethodView.as_view(), name="programming_rust_structure_method"),

    # 
    path("rust/enum/enum/", views_rust.RustEnumWhatIsEnumView.as_view(), name="programming_rust_enum_enum"),
]
