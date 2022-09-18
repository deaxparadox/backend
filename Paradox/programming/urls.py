from django.urls import path

from . import views

urlpatterns = [
    path("", views.ProgramingView.as_view(), name="programming"),
    path("python/concurrency/", views.PythonConcurrencyView.as_view(), name="programming_python_concurrency")
]