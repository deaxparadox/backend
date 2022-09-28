from django.urls import path

from ..views_extend import views_js


urlpatterns = [
    path("js/", views_js.JavascriptView.as_view(), name="programming_js")
]
