from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages

from pms.models.heading import Heading
from django.db import IntegrityError
from pms.models.task import Task
from pms.forms.heading import HeadingModelForm
from pms.forms.task import TaskModelForm




def create_task_view(request):
    if request.method == "POST":
        post_form = TaskModelForm(request.POST)
        if post_form.is_valid():
            try:
                task: Task = post_form.save()
                heading_id = int(post_form.cleaned_data['select_heading'])
                if heading_id > 0:
                    heading = Heading.objects.get(id=heading_id)
                    task.heading = heading
                    task.save()
            except IntegrityError as e:
                messages.add_message(request, messages.INFO, e)
                return redirect(reverse("pms:create_task_view"))
            
            # successfully created
            messages.add_message(request, messages.INFO, "Task created successfully.")
            return redirect(reverse("pms:detail_task_view", kwargs={"id": task.id}))

    form = TaskModelForm()
    return render(request, "pms/task/create.html", {
        "form": form,
        "create_url": Task.get_create_url()
    })


async def detail_task_view(request, id):
    task: Task|None = None
    try:
        task = Task.objects.get(id=id)
    except Task.DoesNotExist as e:
        messages.add_message(request, messages.INFO, "Task does not exist")
        # return render(
        #     request,
        #     "pms/Task/update.html"
        # )
        return redirect(reverse("app:home"))
    except Task.MultipleObjectsReturned as e:
        messages.add_message(request, messages.INFO, "Multiple object returned")
        return render(
            request,
            "pms/task/update.html"
        )
    # form = TaskModelForm(instance=heading)
    # tasks = task.tasks.all()
    return render(
        request,
        "pms/task/detail.html",
        {
            "task": task,
            # "form": form,
            # "tasks": tasks
        }
    )

def edit_task_view(request, id):
    task: Task|None = None
    try:
        task = Task.objects.get(id=id)
    except Heading.DoesNotExist as e:
        messages.add_message(request, messages.INFO, "Heading does not exist")
        return render(
            request,
            "pms/task/update.html"
        )
    except Heading.MultipleObjectsReturned as e:
        messages.add_message(request, messages.INFO, "Multiple object returned")
        return render(
            request,
            "pms/task/update.html"
        )
    form = TaskModelForm(instance=task)
    return render(
        request,
        "pms/task/update.html",
        {
            "form": form
        }
    )


    
def update_task_view(request, id):
    if request.method == "POST":
        task: Task|None = Task.objects.get(id=id)
        post_form = TaskModelForm(request.POST, instance=task)
        if post_form.is_valid():
            post_form.save()
            messages.add_message(request, messages.INFO, "Updated successfully")
            return redirect(reverse("pms:detail_task_view", kwargs={"id": id}))
    try:
        task: Task|None = Task.objects.get(id=id)
    except task.DoesNotExist as e:
        messages.add_message(request, messages.INFO, "Task does not exist")
        # return render(
        #     request,
        #     "pms/heading/update.html"
        # )
        return redirect(reverse("app:home"))
    except Task.MultipleObjectsReturned as e:
        messages.add_message(request, messages.INFO, "Multiple object returned")
        return render(
            request,
            "pms/task/update.html"
        )
    form = TaskModelForm(instance=task)
    # tasks = heading.tasks.all()]
    print(task.get_update_url())
    return render(
        request,
        "pms/task/update.html",
        {
            # "heading": heading
            "form": form,
            "update_url": task.get_update_url()
            # "tasks": tasks
        }
    )