from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.contrib import messages
from border_control2.forms import BorderControl2Form
from border_control2.helpers import create_control, get_results_and_rating
from border_control2.models import BorderControl2, ResultsBC2
from automata_theory.models import KRTime


# Create your views here.
class BorderControl2View(TemplateView):
    # model = BorderControl2
    form_class = BorderControl2Form
    template_name = "test2.html"

    # def get(self, request, *args, **kwargs):
    #     # Проверяем, есть ли уже запись о решении контрольной работы
    #     existing_result = BorderControl2.objects.filter(user=request.user).first()
    #     if existing_result:
    #         messages.warning(request, "Вы уже писали эту контрольную работу")
    #         return redirect("account")
    #     return super().get(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        control = create_control(self.request.user)
        context["number_1"] = control.number1
        context["number_2"] = control.number2
        context["degree_1"] = control.degree_1
        context["degree_2"] = control.degree_2
        context["degree_3"] = control.degree_3
        context["form"] = BorderControl2Form()
        context["pagename"] = "Контрольная работа"

        # Получаем длительность контрольной работы
        kr_time = KRTime.objects.filter(kr_number=2, is_active=True).last()
        if kr_time:
            context["kr_duration"] = str(kr_time.duration)
        else:
            context["kr_duration"] = "01:30:00"  # Значение по умолчанию

        return context

    def post(self, request, *args, **kwargs):
        answers = BorderControl2.objects.filter(user=self.request.user).latest().answers

        results = ResultsBC2.objects.create(
            user=self.request.user,
            straight_1=request.POST["straight_1"],
            reversed_1=request.POST["reversed_1"],
            additional_1=request.POST["additional_1"],
            straight_2=request.POST["straight_2"],
            reversed_2=request.POST["reversed_2"],
            additional_2=request.POST["additional_2"],
            straight_3=request.POST["straight_3"],
            reversed_3=request.POST["reversed_3"],
            additional_3=request.POST["additional_3"],
            straight_4=request.POST["straight_4"],
            reversed_4=request.POST["reversed_4"],
            additional_4=request.POST["additional_4"],
            straight_5=request.POST["straight_5"],
            reversed_5=request.POST["reversed_5"],
            additional_5=request.POST["additional_5"],
            straight_6=request.POST["straight_6"],
            reversed_6=request.POST["reversed_6"],
            additional_6=request.POST["additional_6"],
            straight_7=request.POST["straight_7"],
            reversed_7=request.POST["reversed_7"],
            additional_7=request.POST["additional_7"],
            straight_8=request.POST["straight_8"],
            reversed_8=request.POST["reversed_8"],
            additional_8=request.POST["additional_8"],
            straight_9=request.POST["straight_9"],
            reversed_9=request.POST["reversed_9"],
            additional_9=request.POST["additional_9"],
            straight_10=request.POST["straight_10"],
            reversed_10=request.POST["reversed_10"],
            additional_10=request.POST["additional_10"],
            temp_11=request.POST["temp_11"],
            correction_11=request.POST["correction_11"],
            result_11=request.POST["result_11"],
            realizing_11=request.POST["realizing_11"],
            temp_12=request.POST["temp_12"],
            correction_12=request.POST["correction_12"],
            result_12=request.POST["result_12"],
            realizing_12=request.POST["realizing_12"],
            temp_13=request.POST["temp_13"],
            correction_13=request.POST["correction_13"],
            result_13=request.POST["result_13"],
            realizing_13=request.POST["realizing_13"],
            temp_14=request.POST["temp_14"],
            correction_14=request.POST["correction_14"],
            result_14=request.POST["result_14"],
            realizing_14=request.POST["realizing_14"],
            temp_15=request.POST["temp_15"],
            correction_15=request.POST["correction_15"],
            result_15=request.POST["result_15"],
            realizing_15=request.POST["realizing_15"],
            temp_16=request.POST["temp_16"],
            correction_16=request.POST["correction_16"],
            result_16=request.POST["result_16"],
            realizing_16=request.POST["realizing_16"],
            temp_17=request.POST["temp_17"],
            correction_17=request.POST["correction_17"],
            result_17=request.POST["result_17"],
            realizing_17=request.POST["realizing_17"],
            temp_18=request.POST["temp_18"],
            correction_18=request.POST["correction_18"],
            result_18=request.POST["result_18"],
            realizing_18=request.POST["realizing_18"],
        )

        rating, result_number = get_results_and_rating(answers, results)

        bc2 = BorderControl2.objects.filter(user=request.user).latest()
        bc2.results = results
        bc2.rating = rating
        bc2.result_number = result_number
        bc2.save()

        messages.success(request, "Контрольная работа успешно отправлена")
        return redirect("account")
