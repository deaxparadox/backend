from typing import Any
from django import http
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView
import matplotlib 
import matplotlib.pyplot as plt 
import io, base64
from contextlib import contextmanager

matplotlib.use("Agg")

@contextmanager
def SampleGraph(x: Any = None, y: Any = None):
    if not x:
        x = [x for x in range(10)]
    if not y:
        y = [x+1 for x in x]
    fig, ax = plt.subplots(figsize=(10,4))
    ax.plot(x, y, '--bo')

    flike = io.BytesIO()
    fig.savefig(flike)
    b64 = base64.b64encode(flike.getvalue()).decode()
    yield b64

class Home(TemplateView):
    template_name = "plot/home.html"
    def get(self, request: http.HttpRequest, *args: Any, **kwargs: Any) -> http.HttpResponse:
        # print(self.request.GET.get('a'))
        with SampleGraph() as graph:
            return render(
                request, 
                self.template_name,
                {
                    "graph": graph
                }
            )