from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("index", views.index, name="index"),
    path("sign_up", views.sign_up, name="sign_up"),
    path("login/", auth_views.LoginView.as_view(template_name="registration/login_page.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="login"), name="logout"),
    path("create_note", views.create_note, name="create_note"),
    path(r"update_note/", views.update_note, name="update_note"),
    path("password_change/", auth_views.PasswordChangeView.as_view(template_name="registration/pwd_change_form.html"), name="password_change"),
    path("password_change/done/", auth_views.PasswordChangeDoneView.as_view(template_name="registration/pwd_change_done.html"), name="password_change_done"),
    path("password_reset", auth_views.PasswordResetView.as_view(template_name="registration/pwd_reset_form.html"), name="password_reset"),
    path("password_reset_done", auth_views.PasswordResetDoneView.as_view(template_name="registration/pwd_reset_done.html"), name="password_reset_done"),
    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name="registration/pwd_reset_confirm.html"), name="password_reset_confirm"),
    path("reset/done/", auth_views.PasswordResetCompleteView.as_view(template_name="registration/pwd_reset_complete.html"), name="password_reset_complete"),
    path("404", views.error_page_404, name="error_page_404"),
]