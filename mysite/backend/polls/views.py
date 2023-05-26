from typing import Any
from django.utils import timezone
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Question, Choice

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
    
#     return render(request, "polls/index.html", {
#         "latest_question_list": latest_question_list
#     })

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self) -> QuerySet[Any]:
        # return super().get_queryset().order_by("-pub_data")[:5]
        return Question.objects.filter(pub_data__lte=timezone.now()).order_by('-pub_date')[:5]

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")    
    return render(request, "polls/details.html", {
        "question": question
    })

def results(reqeust, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(
        reqeust, 
        "polls/results.html",
        {
            "question": question,
        }
    )

def vote(request, question_id):
    question: Question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/details.html",
            {
                "question": question,
                "error_messages": "You didn't select a choice.",
            }
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(
            reverse("polls:result", args=(question.id,))
        )