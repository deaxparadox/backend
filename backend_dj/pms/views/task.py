from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages

from pms.models.heading import Heading
from pms.models.task import Task
from pms.forms.heading import HeadingModelForm
from pms.forms.task import TaskModelForm




def create_task_view(request):
    form = TaskModelForm()
    return render(request, "pms/create/task.html", {
        "form": form
    })



def edit_task_view(request, id):
    task: Task|None = None
    try:
        task = Task.objects.get(id=id)
    except Heading.DoesNotExist as e:
        messages.add_message(request, messages.INFO, "Heading does not exist")
        return render(
            request,
            "pms/edit/task.html"
        )
    except Heading.MultipleObjectsReturned as e:
        messages.add_message(request, messages.INFO, "Multiple object returned")
        return render(
            request,
            "pms/edit/task.html"
        )
    form = TaskModelForm(instance=task)
    return render(
        request,
        "pms/edit_task.html",
        {
            "form": form
        }
    )