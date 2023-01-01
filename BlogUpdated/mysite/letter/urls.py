from django.urls import path 

from .views import LetterDetailView, LetterListView, LetterTestView

app_name = "letter"

urlpatterns = [
    path("", LetterListView, name="letter_list"),
    path("<slug:slug>", LetterDetailView, name="letter_detail"),
    path('test/', LetterTestView, name="letter_test")
]
