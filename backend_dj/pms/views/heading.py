from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages


from channels.db import database_sync_to_async

from pms.models.heading import Heading
from pms.models.task import Task
from pms.forms.heading import HeadingModelForm
from pms.forms.task import TaskModelForm


def get_all_heading():
    """
    Return queryset, ordering by created date in reverse order.
    """
    return Heading.objects.all().order_by('-created')

async def async_get_all_heading():
    return await database_sync_to_async(get_all_heading)()

async def home_view(request):
    headings = await async_get_all_heading()
    # headings = []
    if len(headings) == 0:
        messages.add_message(request, messages.INFO, "No task created :(")

    return render(
        request,
        "pms/heading/index.html",
        {
            "headings": headings
        }
    )

async def create_heading_view(request):
    if request.method == "POST":
        post_form = HeadingModelForm(request.POST)
        if post_form.is_valid():
            post_form.save()
            return redirect(reverse("pms:home"))
    form = HeadingModelForm()
    return render(request, "pms/heading/create.html", {
        "form": form,
        "create_url": Heading.get_create_url(),
    })


def update_heading_view(request, id):
    if request.method == "POST":
        heading: Heading|None = Heading.objects.get(id=id)
        post_form = HeadingModelForm(request.POST, instance=heading)
        if post_form.is_valid():
            post_form.save()
            messages.add_message(request, messages.INFO, "Updated successfully")
            return redirect(reverse("pms:detail_heading_view", kwargs={"id": id}))
    try:
        heading: Heading|None = Heading.objects.get(id=id)
    except Heading.DoesNotExist as e:
        messages.add_message(request, messages.INFO, "Heading does not exist")
        # return render(
        #     request,
        #     "pms/heading/update.html"
        # )
        return redirect(reverse("app:home"))
    except Heading.MultipleObjectsReturned as e:
        messages.add_message(request, messages.INFO, "Multiple object returned")
        return render(
            request,
            "pms/heading/update.html"
        )
    form = HeadingModelForm(instance=heading)
    # tasks = heading.tasks.all()
    return render(
        request,
        "pms/heading/update.html",
        {
            # "heading": heading
            "form": form,
            "update_url": heading.get_update_url()
            # "tasks": tasks
        }
    )


async def detail_heading_view(request, id):
    heading: Heading|None = None
    try:
        heading = Heading.objects.get(id=id)
    except Heading.DoesNotExist as e:
        messages.add_message(request, messages.INFO, "Heading does not exist")
        # return render(
        #     request,
        #     "pms/heading/update.html"
        # )
        return redirect(reverse("app:home"))
    except Heading.MultipleObjectsReturned as e:
        messages.add_message(request, messages.INFO, "Multiple object returned")
        return render(
            request,
            "pms/heading/update.html"
        )
    form = HeadingModelForm(instance=heading)
    tasks = heading.tasks.all()
    return render(
        request,
        "pms/heading/detail.html",
        {
            "heading": heading,
            "form": form,
            "tasks": tasks
        }
    )