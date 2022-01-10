from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import CreateView, View
from .forms import CustomUserCreationForm, UserUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "signup.html"


class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, "profile.html", {"user": request.user})


class ProfileUpdateView(LoginRequiredMixin, View):
    def get(self, request):
        user_update_form = UserUpdateForm(instance=request.user)
        return render(request, "profile_edit.html", {"form": user_update_form})

    def post(self, request):
        user_update_form = UserUpdateForm(
            instance=request.user,
            data=request.POST,
            files=request.FILES
        )

        if user_update_form.is_valid():
            user_update_form.save()
            messages.success(request, "You have successfully updated your profile.")

            return redirect("profile")

        return render(request, "profile_edit.html", {"form": user_update_form})