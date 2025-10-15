from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.contrib import messages
from border_control1.forms import BorderControl1Form
from border_control1.helpers import create_control, get_results_and_rating, convert_integer_part
from border_control1.models import BorderControl1, ResultsBC1
from automata_theory.models import KRTime


# Create your views here.
class BorderControl1View(TemplateView):
    # model = BorderControl2
    form_class = BorderControl1Form
    template_name = "test1.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        control = create_control(self.request.user)
        context["number"] = control.number
        context["number_sec"] = control.number_sec
        context["number_trd_bin"] = convert_integer_part(control.number_trd,2)
        context["number_fth_p"] = convert_integer_part(control.number_fth, control.p_system)
        context["number_main"] = int(control.number)
        context["number_add"] = int((control.number * 1000) % 1000)
        context["p_system"] = control.p_system
        context["form"] = BorderControl1Form()
        context["pagename"] = "Контрольная работа №1"

        # Получаем длительность контрольной работы
        kr_time = KRTime.objects.filter(kr_number=1, is_active=True).first()
        if kr_time:
            context["kr_duration"] = str(kr_time.duration)
        else:
            context["kr_duration"] = "00:35:00"  # Значение по умолчанию

        return context

    def post(self, request, *args, **kwargs):
        answers = BorderControl1.objects.filter(user=self.request.user).latest().answers
        results = ResultsBC1.objects.create(
            user=self.request.user,
            float_bin=request.POST["float_bin"],
            float_oct=request.POST["float_oct"],
            float_hex=request.POST["float_hex"],
            int_bin=request.POST["int_bin"],
            int_oct=request.POST["int_oct"],
            int_hex=request.POST["int_hex"],
            int_sec_bin=request.POST["int_sec_bin"],
            int_sec_p=request.POST["int_sec_p"],
            int_trd=request.POST["int_trd"],
            int_trd_p=request.POST["int_trd_p"],
            int_fth=request.POST["int_fth"],
            int_fth_bin=request.POST["int_fth_bin"],
        )

        rating, result_number = get_results_and_rating(answers, results)

        bc1 = BorderControl1.objects.filter(user=self.request.user).latest()
        bc1.results=results
        bc1.rating=rating
        bc1.result_number=result_number
        bc1.save()
        
        messages.success(request, "Контрольная работа успешно отправлена")
        return redirect("account")
