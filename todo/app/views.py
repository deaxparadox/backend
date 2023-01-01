from typing import Any
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import QuerySet

from . import models
from . import forms

class Home(LoginRequiredMixin, generic.ListView):
    login_url = "/accounts/login/"
    template_name: str = "app/index.html"
    model = models.Todo
    context_object_name = "todos"
    

    def get_queryset(self) -> QuerySet[Any]:
        return super().get_queryset()

class Add(LoginRequiredMixin, generic.FormView, generic.CreateView):
    login_url = "/accounts/login/"
    template_name: str = "app/add.html"
    model = models.Todo
    form_class = forms.Todo
    success_url = "/"

    def get(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        print(self.request.user)
        return render(
            request,
            self.template_name,
            {
                "form": self.form_class
            }
        )

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        userid = User.objects.get(username=self.request.user)
        form = forms.Todo(self.request.POST)
        if form.is_valid():
            cform = form.cleaned_data
            title = cform.get('title')
            memo = cform.get("memo")
            status = cform.get("status")
            models.Todo.object.create(
                user=userid,
                title=title,
                memo=memo,
                status=status
            )
            
        return redirect("/")
        
