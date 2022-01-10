from django.urls import path

from .views import SignUpView, ProfileUpdateView, ProfileView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("profile/edit/", ProfileUpdateView.as_view(), name="profile-edit"),
]