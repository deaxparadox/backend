from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages


from channels.db import database_sync_to_async

from pms.models.heading import Heading
from pms.models.task import Task
from pms.forms.heading import HeadingModelForm
from pms.forms.task import TaskModelForm


def get_all_heading():
    return Heading.objects.all()

async def async_get_all_heading():
    return await database_sync_to_async(get_all_heading)()

async def home_view(request):
    headings = await async_get_all_heading()
    # headings = []
    if len(headings) == 0:
        messages.add_message(request, messages.INFO, "No task created :(")

    return render(
        request,
        "pms/index.html",
        {
            "headings": headings
        }
    )

def create_heading_view(request):
    form = HeadingModelForm()
    return render(request, "pms/create_heading.html", {
        "form": form
    })


def edit_heading_view(request, id):
    heading: Heading|None = None
    try:
        heading = Heading.objects.get(id=id)
    except Heading.DoesNotExist as e:
        messages.add_message(request, messages.INFO, "Heading does not exist")
        # return render(
        #     request,
        #     "pms/edit/heading.html"
        # )
        return redirect(reverse("app:home"))
    except Heading.MultipleObjectsReturned as e:
        messages.add_message(request, messages.INFO, "Multiple object returned")
        return render(
            request,
            "pms/edit/heading.html"
        )
    form = HeadingModelForm(instance=heading)
    tasks = heading.tasks.all()
    return render(
        request,
        "pms/edit_heading.html",
        {
            # "heading": heading
            "form": form,
            "tasks": tasks
        }
    )
