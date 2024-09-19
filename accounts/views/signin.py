from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

from accounts.forms import SignInForm


class SignInView(View):
    """ User sign-in view """

    template_name = "accounts/signin.html"
    form_class = SignInForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        context = {"form": form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                messages.success(request, "Authentication successful! Redirecting to dashboard...")
                return render(request, self.template_name, {"form": form})
            else:
                messages.error(request, "Authentication failed. Invalid email or password.")
        context = {"form": form}
        return render(request, self.template_name, context)
