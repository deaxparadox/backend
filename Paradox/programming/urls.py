from django.urls import path

# from .view_extend import py, rust
from .urls_extend import urls_py, urls_rust, urls_js, urls_c, urls_projects, urls_dsa
from . import views

urlpatterns = [
    path("", views.ProgramingView.as_view(), name="programming"),
    
    # path("python/concurrency/", py.PythonConcurrencyView.as_view(), name="programming_python_concurrency")
] + urls_py.urlpatterns + urls_rust.urlpatterns + urls_js.urlpatterns + urls_c.urlpatterns + urls_projects.urlpatterns + urls_dsa.urlpatterns
