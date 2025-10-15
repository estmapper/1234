from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.urls import path
from django.shortcuts import get_object_or_404
from django.template.response import TemplateResponse

from border_control2.models import *


# Register your models here.
class BorderControl2Admin(admin.ModelAdmin):
    list_display = [
        "view_results_link",
        "user",
        "number1",
        "number2",
        "degree_1",
        "degree_2",
        "degree_3",
        "answers",
        "results",
        "result_number",
        "rating",
        "create_date",
    ]
    search_fields = ("user__last_name",)

    readonly_fields = ("id", "view_results_link")

    def view_results_link(self, obj):
        url = reverse("admin:bordercontrol2_results_view", args=[obj.id])
        return format_html('<a href="{}">Просмотреть результаты</a>', url)

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path(
                "<uuid:object_id>/results/",
                self.admin_site.admin_view(self.results_view),
                name="bordercontrol2_results_view",
            ),
        ]
        return custom_urls + urls

    def results_view(self, request, object_id):

        obj = get_object_or_404(BorderControl2, id=object_id)

        context = {
            **self.admin_site.each_context(request),
            "title": f"Результаты для работы {object_id}",
            "object": obj,
            "opts": self.model._meta,
            "answers": obj.answers,
            "user_answers": obj.results,
        }

        return TemplateResponse(
            request, "admin/bordercontrol2/results_table.html", context
        )


class AnswersBC2Admin(admin.ModelAdmin):
    list_display = [
        "straight_1",
        "reversed_1",
        "additional_1",
        "straight_2",
        "reversed_2",
        "additional_2",
        "straight_3",
        "reversed_3",
        "additional_3",
        "straight_4",
        "reversed_4",
        "additional_4",
        "straight_5",
        "reversed_5",
        "additional_5",
        "straight_6",
        "reversed_6",
        "additional_6",
        "straight_7",
        "reversed_7",
        "additional_7",
        "straight_8",
        "reversed_8",
        "additional_8",
        "straight_9",
        "reversed_9",
        "additional_9",
        "straight_10",
        "reversed_10",
        "additional_10",
        "temp_11",
        "correction_11",
        "result_11",
        "realizing_11",
        "temp_12",
        "correction_12",
        "result_12",
        "realizing_12",
        "temp_13",
        "correction_13",
        "result_13",
        "realizing_13",
        "temp_14",
        "correction_14",
        "result_14",
        "realizing_14",
        "temp_15",
        "correction_15",
        "result_15",
        "realizing_15",
        "temp_16",
        "correction_16",
        "result_16",
        "realizing_16",
        "temp_17",
        "correction_17",
        "result_17",
        "realizing_17",
        "temp_18",
        "correction_18",
        "result_18",
        "realizing_18",
        "create_date",
    ]


class ResultsBC2Admin(admin.ModelAdmin):
    list_display = [
        "straight_1",
        "reversed_1",
        "additional_1",
        "straight_2",
        "reversed_2",
        "additional_2",
        "straight_3",
        "reversed_3",
        "additional_3",
        "straight_4",
        "reversed_4",
        "additional_4",
        "straight_5",
        "reversed_5",
        "additional_5",
        "straight_6",
        "reversed_6",
        "additional_6",
        "straight_7",
        "reversed_7",
        "additional_7",
        "straight_8",
        "reversed_8",
        "additional_8",
        "straight_9",
        "reversed_9",
        "additional_9",
        "straight_10",
        "reversed_10",
        "additional_10",
        "temp_11",
        "correction_11",
        "result_11",
        "realizing_11",
        "temp_12",
        "correction_12",
        "result_12",
        "realizing_12",
        "temp_13",
        "correction_13",
        "result_13",
        "realizing_13",
        "temp_14",
        "correction_14",
        "result_14",
        "realizing_14",
        "temp_15",
        "correction_15",
        "result_15",
        "realizing_15",
        "temp_16",
        "correction_16",
        "result_16",
        "realizing_16",
        "temp_17",
        "correction_17",
        "result_17",
        "realizing_17",
        "temp_18",
        "correction_18",
        "result_18",
        "realizing_18",
        "create_date",
    ]


class RatingBC2Admin(admin.ModelAdmin):
    list_display = [
        "is_active",
        "create_date",
        "update_date",
    ]
    list_filter = ("is_active",)
    search_fields = ("id",)
    ordering = ("-create_date",)
    readonly_fields = ["id", "create_date", "update_date"]

    fieldsets = (
        (None, {"fields": ("is_active",)}),
        (
            "Коды A / -A / B / -B",
            {
                "fields": (
                    "straight_1", "reversed_1", "additional_1",
                    "straight_2", "reversed_2", "additional_2",
                    "straight_3", "reversed_3", "additional_3",
                    "straight_4", "reversed_4", "additional_4",
                )
            },
        ),
        (
            "Степенные варианты",
            {
                "fields": (
                    "straight_5", "reversed_5", "additional_5",
                    "straight_6", "reversed_6", "additional_6",
                    "straight_7", "reversed_7", "additional_7",
                    "straight_8", "reversed_8", "additional_8",
                    "straight_9", "reversed_9", "additional_9",
                    "straight_10", "reversed_10", "additional_10",
                )
            },
        ),
        (
            "Операции с дополнительным кодом (11–14)",
            {
                "fields": (
                    "temp_11", "correction_11", "result_11", "realizing_11",
                    "temp_12", "correction_12", "result_12", "realizing_12",
                    "temp_13", "correction_13", "result_13", "realizing_13",
                    "temp_14", "correction_14", "result_14", "realizing_14",
                )
            },
        ),
        (
            "Операции с обратным кодом (15–18)",
            {
                "fields": (
                    "temp_15", "correction_15", "result_15", "realizing_15",
                    "temp_16", "correction_16", "result_16", "realizing_16",
                    "temp_17", "correction_17", "result_17", "realizing_17",
                    "temp_18", "correction_18", "result_18", "realizing_18",
                )
            },
        ),
        ("Служебные", {"fields": ("id", "create_date", "update_date")}),
    )


admin.site.register(BorderControl2, BorderControl2Admin)
admin.site.register(AnswersBC2, AnswersBC2Admin)
admin.site.register(ResultsBC2, ResultsBC2Admin)
admin.site.register(RatingBC2, RatingBC2Admin)
