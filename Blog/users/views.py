from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from django.conf import settings


from typing import *

from . import models
from . import forms

class SignUpView(generic.CreateView):
    template_name: str = 'registration/signup.html'
    success_url = reverse_lazy("login")
    form_class = forms.CUserCreationFrom

class ProfileUpdate(LoginRequiredMixin ,generic.UpdateView):
    template_name: str = 'registration/profile.html'
    success_url = reverse_lazy("login")
    # form_class = ["email"]
    fields = ["first_name", "last_name", "email"]
    model = models.CUser
    context_object_name: str = "user_detail"
    login_url: Any = "login"

    