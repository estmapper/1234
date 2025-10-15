from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin

from automata_theory.forms import LoginUserForm, RegistrationForm
from border_control1.models import BorderControl1
from border_control1.helpers import convert_integer_part
from border_control2.models import BorderControl2, ResultsBC2, AnswersBC2
from .models import CustomUser


class MainPageView(TemplateView):
    template_name = "mainpage.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["pagename"] = "Главная страница"
        return context

    def get(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect("login")

        return super().get(request, *args, **kwargs)


class PageView(TemplateView):
    template_name = "index.html"


# Create your views here.
class BorderControlView(TemplateView):
    template_name = "test.html"

    def get(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect("login")

        return super().get(request, *args, **kwargs)


class AccountView(TemplateView):
    template_name = "personal-account.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context["pagename"] = "Аккаунт"
        context["user"] = self.request.user

        result1 = BorderControl1.objects.filter(user=self.request.user).first()
        result2 = BorderControl2.objects.filter(user=self.request.user).first()

        context["kr_first"] = result1.result_number if result1 else "-"
        context["kr_second"] = result2.result_number if result2 else "-"
        context["kr_third"] = "no data"
        return context

    def get(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect("login")

        return super().get(request, *args, **kwargs)


class ExtendedLoginView(LoginView):
    form_class = LoginUserForm
    template_name = "login.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["pagename"] = "Вход"
        return context

    def get_success_url(self):
        return reverse_lazy("main")

    def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        response = super(LoginView, self).post(request, *args, **kwargs)
        if request.user.is_authenticated:
            messages.success(request, "Вы вошли в свой аккаунт")
            return redirect("main")
        else:
            messages.error(request, "Неверный логин или пароль")
        return response


class RegisterView(FormView):
    form_class = RegistrationForm
    template_name = "register.html"
    success_url = reverse_lazy("main")

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("main")
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        messages.success(self.request, "Регистрация прошла успешно")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Исправьте ошибки в форме")
        return super().form_invalid(form)


def logout_view(request):
    logout(request)
    return redirect("login")


class KRDetailView(TemplateView):
    template_name = "kr_detail.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        kr_number = self.kwargs.get("kr_number")
        user = self.request.user

        if kr_number == 1:
            result = BorderControl1.objects.filter(user=user).latest()
            context["kr_number"] = "Контрольная работа №1"
            context["result"] = result
            context["answers"] = result.answers
            context["user_answers"] = result.results
            context["number_trd"] = convert_integer_part(result.number_trd, 2)
            context["number_fth"] = convert_integer_part(result.number_fth, result.p_system)
            context["number"] = int(result.number)
            context["number_add"] = int((result.number*1000)%1000)
        elif kr_number == 2:
            result = BorderControl2.objects.filter(user=user).latest()
            context["kr_number"] = "Контрольная работа №2"
            context["result"] = result
            context["answers"] = result.answers
            context["user_answers"] = result.results
        else:
            context["kr_number"] = "Контрольная работа №3"
            context["result"] = None
            context["answers"] = None
            context["user_answers"] = None

        context["pagename"] = context["kr_number"]
        return context

    def get(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect("login")
        return super().get(request, *args, **kwargs)
