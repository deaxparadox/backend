from django.urls import reverse
from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect

from .models import Question, Choice

def index(request):
    questions = Question.objects.all()
    return render(request, "polls/index.html", {
        "questions": questions
    })

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question doesnot exits.")
    
    return render(request, "polls/detail.html", {
        "question": question,
    })

def vote(request, question_id):
    question = Question.objects.get(pk=question_id)

    choice = request.POST["choice"]
    try:
        selected_choice = question.choice_set.get(pk=choice)
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "Question doesn't exists."
            }
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(
            reverse("result", args=(question.id,)),
        )
    
def result(request, question_id):
    question = Question.objects.get(pk=question_id)
    return render(request, "polls/result.html", {
        "question": question
    })