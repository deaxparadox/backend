from django.urls import path

from ..views_extend import views_c


urlpatterns = [
    path("c/", views_c.CView.as_view(), name="programming_c")
]
