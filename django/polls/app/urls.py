from django.urls import path

from . import views
from . import generic_views

app_name = "app"

try:
    urlpatterns = [
        # ex: /polls/
        path("", generic_views.IndexView.as_view(), name="index"),
    
        # ex: /polls/5/
        path("<int:pk>/", generic_views.DetailView.as_view(), name="detail"),
    
        # ex: /polls/5/results/
        path("<int:pk>/results/", generic_views.ResultsView.as_view(), name="results"),

    ]
except:

    urlpatterns = [
        # ex: /polls/
        path("", views.index, name="index"),
    
        # ex: /polls/5/
        path("<int:pk>/", views.detail, name="detail"),
    
        # ex: /polls/5/results/
        path("<int:pk>/results/", views.results, name="results"),
    
       
    ]

urlpatterns += [
     # ex: /polls/5/vote/
    path("<int:pk>/vote/", views.vote, name="vote"),
]