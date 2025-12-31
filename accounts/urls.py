from django.urls import path
from accounts import views

urlpatterns = [
    path("", views.login_user, name="login_user"),
    path("register/", views.register, name="register"),
    path("logout/", views.logout, name="logout"),
    path("profile/", views.profile, name="profile"),
    path("edit-profile/", views.edit_profile, name="edit_profile"),
    path("change-password/", views.change_password, name="change_password"),
]
