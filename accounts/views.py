from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import render, redirect
from django.views.generic import CreateView, FormView

from .forms import LoginForm, RegisterForm


# Create your views here.
class LoginView(FormView):
    form_class = LoginForm
    success_url = '/'
    template_name = "accounts/login.html"

    def form_valid(self, form):
        request = self.request
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        return super(LoginView, self).form_invalid(form)



class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'accounts/register.html'
    success_url = '/login/'


