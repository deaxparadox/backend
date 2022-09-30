from django.urls import path 

from ..views_extend import views_dsa
urlpatterns = [
    path("dsa/linked_list/stack/", views_dsa.DSALinkedListStackView.as_view(), name="programming_dsa_linkedlist_stack")
]
