from django.shortcuts import render
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from accounts.forms import CustomUserCreationForm
from django.contrib.auth import login
from django.shortcuts import redirect

from accounts.forms import AuthenticationForm


class RegisterView(FormView):
    """View for registering a new user."""
    template_name = "accounts/register.html"
    form_class = CustomUserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy("pdf:resume-list")

    def form_valid(self, form):
        user = form.save()  # This saves the user when the form is valid
        if user is not None:
            login(self.request, user)  # Log the user in after successful registration
        return super().form_valid(form)

    def form_invalid(self, form):
        # This method is automatically called when the form has errors
        return self.render_to_response(self.get_context_data(form=form))

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("pdf:resume-list")
        return super().get(*args, **kwargs)


class LoginView(auth_views.LoginView):
    form_class = AuthenticationForm
    template_name = "accounts/login.html"
    redirect_authenticated_user = True


class LogoutView(auth_views.LogoutView):
    pass

class PasswordResetView(auth_views.PasswordResetView):
    email_template_name = "accounts/password_reset_email.html"
    html_email_template_name = "accounts/password_reset_email.html"
    success_url = reverse_lazy("accounts:password_reset_done")

class PasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    success_url = reverse_lazy("accounts:password_reset_complete")
