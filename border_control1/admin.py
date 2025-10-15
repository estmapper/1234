from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.urls import path
from django.shortcuts import get_object_or_404
from django.template.response import TemplateResponse
from border_control1.models import *


# Register your models here.
class BorderControl1Admin(admin.ModelAdmin):
    list_display = [
        "view_results_link",
        "user",
        #"attempt",
        "number",
        "number_sec",
        "number_trd",
        "number_fth",
        "p_system",
        "answers_link",
        "results_link",
        "result_number",
        "rating",
    ]
    list_display_links = ("view_results_link", "user")
    list_editable = ("p_system", "result_number", "rating")
    list_filter = (
        "p_system",
        "rating",
        "result_number",
        ("results", admin.EmptyFieldListFilter),
        ("user", admin.RelatedOnlyFieldListFilter),
    )
    search_fields = (
        "user__last_name",
        "user__first_name",
        "user__username",
        "user__email",
        "id",
    )
    list_select_related = ("user", "answers", "results")
    list_per_page = 50
    ordering = ("-rating", "-result_number")
    autocomplete_fields = ("answers", "results")
    raw_id_fields = ("user",)

    readonly_fields = ("id", "view_results_link")

    def view_results_link(self, obj):
        url = reverse("admin:bordercontrol1_results_view", args=[obj.id])
        return format_html('<a href="{}">Просмотреть результаты</a>', url)

    def answers_link(self, obj):
        if not obj.answers:
            return "—"
        url = reverse("admin:border_control1_answersbc1_change", args=[obj.answers_id])
        return format_html('<a href="{}">Ожидаемые</a>', url)

    def results_link(self, obj):
        if not obj.results:
            return "—"
        url = reverse("admin:border_control1_resultsbc1_change", args=[obj.results_id])
        return format_html('<a href="{}">Ответы</a>', url)

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path(
                "<uuid:object_id>/results/",
                self.admin_site.admin_view(self.results_view),
                name="bordercontrol1_results_view",
            ),
        ]
        return custom_urls + urls

    def results_view(self, request, object_id):

        obj = get_object_or_404(BorderControl1, id=object_id)

        context = {
            **self.admin_site.each_context(request),
            "title": f"Результаты для работы {object_id}",
            "object": obj,
            "opts": self.model._meta,
            "answers": obj.answers,
            "user_answers": obj.results,
        }

        return TemplateResponse(
            request, "admin/bordercontrol1/results_table.html", context
        )


class AnswersBC1Admin(admin.ModelAdmin):
    list_display = [
        "user",
        "float_bin",
        "float_oct",
        "float_hex",
        "int_bin",
        "int_oct",
        "int_hex",
        "int_sec_bin",
        "int_sec_p",
        "int_trd",
        "int_trd_p",
        "int_fth",
        "int_fth_bin",
    ]
    search_fields = (
        "user__last_name",
        "user__first_name",
        "user__username",
        "user__email",
        "id",
    )
    list_filter = (("user", admin.RelatedOnlyFieldListFilter),)
    list_select_related = ("user",)
    list_per_page = 50


class RatingBC1Admin(admin.ModelAdmin):
    list_display = [
        "is_active",
        "float_bin", "float_oct", "float_hex",
        "int_bin", "int_oct", "int_hex",
        "int_sec_bin", "int_sec_p",
        "int_trd", "int_trd_p",
        "int_fth", "int_fth_bin",
        "create_date", "update_date",
    ]
    list_filter = ("is_active",)
    search_fields = ("id",)
    ordering = ("-create_date",)

class ResultsBC1Admin(admin.ModelAdmin):
    list_display = [
        "user",
        "float_bin",
        "float_oct",
        "float_hex",
        "int_bin",
        "int_oct",
        "int_hex",
        "int_sec_bin",
        "int_sec_p",
        "int_trd",
        "int_trd_p",
        "int_fth",
        "int_fth_bin",
    ]
    search_fields = (
        "user__last_name",
        "user__first_name",
        "user__username",
        "user__email",
        "id",
    )
    list_filter = (("user", admin.RelatedOnlyFieldListFilter),)
    list_select_related = ("user",)
    list_per_page = 50


admin.site.register(BorderControl1, BorderControl1Admin)
admin.site.register(AnswersBC1, AnswersBC1Admin)
admin.site.register(ResultsBC1, ResultsBC1Admin)
admin.site.register(RatingBC1, RatingBC1Admin)
