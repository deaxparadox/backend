from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.template import loader
from django.contrib import messages
from django.utils import timezone

from .models import Question, Choice


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "app/index.html", context)

def detail(request, pk):
    question = get_object_or_404(Question, pk=pk)
    return render(request, "app/detail.html", {"question": question})

def results(request, pk):
    question = get_object_or_404(Question, pk=pk)
    return render(
        request,
        "app/results.html",
        {
            "question": question
        }
    )


def vote(request, pk):
    question = get_object_or_404(Question, pk=pk)

    try:
        selected_choice = question.choices.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "app/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice."
            }
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("app:results", args=(question.id,)))


def create_question(request):
    match request.method:
        case "POST":
            # get question from request POST
            question = request.POST["question"]

            # get choices from request POST
            choice1 = request.POST["choice1"]
            choice2 = request.POST["choice2"]
            choice3 = request.POST["choice3"]
            choice4 = request.POST["choice4"]


            if question:
                q = Question.objects.create(question_text=question, pub_date=timezone.now())    
                q.choices.create(choice_text=choice1)
                q.choices.create(choice_text=choice2)
                q.choices.create(choice_text=choice3)
                q.choices.create(choice_text=choice4)
            else:
                messages.add_message(request, messages.INFO, "Invalid question!")
                return HttpResponseRedirect(reverse("app:create_question"))
            
            messages.add_message(request, messages.INFO, "Post method.")
            return HttpResponseRedirect(reverse("app:index"))
        
        case default:
            return render(
                request,
                "app/question/create.html",
                {}
            )