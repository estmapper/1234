import uuid
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from automata_theory.models import CustomUser


class RatingBC2(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    is_active = models.BooleanField(verbose_name="Активная система оценивания", default=True)

    # Per-field weights for BC2 (answers/results)
    # Codes for A, -A, B, -B
    straight_1 = models.IntegerField(verbose_name="Вес: Прямой код A", default=1)
    reversed_1 = models.IntegerField(verbose_name="Вес: Обратный код A", default=1)
    additional_1 = models.IntegerField(verbose_name="Вес: Дополнительный код A", default=1)

    straight_2 = models.IntegerField(verbose_name="Вес: Прямой код -A", default=1)
    reversed_2 = models.IntegerField(verbose_name="Вес: Обратный код -A", default=1)
    additional_2 = models.IntegerField(verbose_name="Вес: Дополнительный код -A", default=1)

    straight_3 = models.IntegerField(verbose_name="Вес: Прямой код B", default=1)
    reversed_3 = models.IntegerField(verbose_name="Вес: Обратный код B", default=1)
    additional_3 = models.IntegerField(verbose_name="Вес: Дополнительный код B", default=1)

    straight_4 = models.IntegerField(verbose_name="Вес: Прямой код -B", default=1)
    reversed_4 = models.IntegerField(verbose_name="Вес: Обратный код -B", default=1)
    additional_4 = models.IntegerField(verbose_name="Вес: Дополнительный код -B", default=1)

    # Degree variants
    straight_5 = models.IntegerField(verbose_name="Вес: Прямой код A*2^-n", default=1)
    reversed_5 = models.IntegerField(verbose_name="Вес: Обратный код A*2^-n", default=1)
    additional_5 = models.IntegerField(verbose_name="Вес: Дополнительный код A*2^-n", default=1)

    straight_6 = models.IntegerField(verbose_name="Вес: Прямой код A*2^m", default=1)
    reversed_6 = models.IntegerField(verbose_name="Вес: Обратный код A*2^m", default=1)
    additional_6 = models.IntegerField(verbose_name="Вес: Дополнительный код A*2^m", default=1)

    straight_7 = models.IntegerField(verbose_name="Вес: Прямой код A*2^q", default=1)
    reversed_7 = models.IntegerField(verbose_name="Вес: Обратный код A*2^q", default=1)
    additional_7 = models.IntegerField(verbose_name="Вес: Дополнительный код A*2^q", default=1)

    straight_8 = models.IntegerField(verbose_name="Вес: Прямой код B*2^-n", default=1)
    reversed_8 = models.IntegerField(verbose_name="Вес: Обратный код B*2^-n", default=1)
    additional_8 = models.IntegerField(verbose_name="Вес: Дополнительный код B*2^-n", default=1)

    straight_9 = models.IntegerField(verbose_name="Вес: Прямой код B*2^m", default=1)
    reversed_9 = models.IntegerField(verbose_name="Вес: Обратный код B*2^m", default=1)
    additional_9 = models.IntegerField(verbose_name="Вес: Дополнительный код B*2^m", default=1)

    straight_10 = models.IntegerField(verbose_name="Вес: Прямой код B*2^q", default=1)
    reversed_10 = models.IntegerField(verbose_name="Вес: Обратный код B*2^q", default=1)
    additional_10 = models.IntegerField(verbose_name="Вес: Дополнительный код B*2^q", default=1)

    # Additional code operations (11-14)
    temp_11 = models.IntegerField(verbose_name="Вес: A(доп)+B(доп) промежуточный", default=1)
    correction_11 = models.IntegerField(verbose_name="Вес: Коррекция A(доп)+B(доп)", default=1)
    result_11 = models.IntegerField(verbose_name="Вес: A(доп)+B(доп) итоговый", default=1)
    realizing_11 = models.IntegerField(verbose_name="Вес: A(доп)+B(доп) осмысление", default=1)

    temp_12 = models.IntegerField(verbose_name="Вес: -A(доп)+B(доп) промежуточный", default=1)
    correction_12 = models.IntegerField(verbose_name="Вес: Коррекция -A(доп)+B(доп)", default=1)
    result_12 = models.IntegerField(verbose_name="Вес: -A(доп)+B(доп) итоговый", default=1)
    realizing_12 = models.IntegerField(verbose_name="Вес: -A(доп)+B(доп) осмысление", default=1)

    temp_13 = models.IntegerField(verbose_name="Вес: A(доп)-B(доп) промежуточный", default=1)
    correction_13 = models.IntegerField(verbose_name="Вес: Коррекция A(доп)-B(доп)", default=1)
    result_13 = models.IntegerField(verbose_name="Вес: A(доп)-B(доп) итоговый", default=1)
    realizing_13 = models.IntegerField(verbose_name="Вес: A(доп)-B(доп) осмысление", default=1)

    temp_14 = models.IntegerField(verbose_name="Вес: -A(доп)-B(доп) промежуточный", default=1)
    correction_14 = models.IntegerField(verbose_name="Вес: Коррекция -A(доп)-B(доп)", default=1)
    result_14 = models.IntegerField(verbose_name="Вес: -A(доп)-B(доп) итоговый", default=1)
    realizing_14 = models.IntegerField(verbose_name="Вес: -A(доп)-B(доп) осмысление", default=1)

    # Reverse code operations (15-18)
    temp_15 = models.IntegerField(verbose_name="Вес: A(обр)+B(обр) промежуточный", default=1)
    correction_15 = models.IntegerField(verbose_name="Вес: Коррекция A(обр)+B(обр)", default=1)
    result_15 = models.IntegerField(verbose_name="Вес: A(обр)+B(обр) итоговый", default=1)
    realizing_15 = models.IntegerField(verbose_name="Вес: A(обр)+B(обр) осмысление", default=1)

    temp_16 = models.IntegerField(verbose_name="Вес: -A(обр)+B(обр) промежуточный", default=1)
    correction_16 = models.IntegerField(verbose_name="Вес: Коррекция -A(обр)+B(обр)", default=1)
    result_16 = models.IntegerField(verbose_name="Вес: -A(обр)+B(обр) итоговый", default=1)
    realizing_16 = models.IntegerField(verbose_name="Вес: -A(обр)+B(обр) осмысление", default=1)

    temp_17 = models.IntegerField(verbose_name="Вес: A(обр)-B(обр) промежуточный", default=1)
    correction_17 = models.IntegerField(verbose_name="Вес: Коррекция A(обр)-B(обр)", default=1)
    result_17 = models.IntegerField(verbose_name="Вес: A(обр)-B(обр) итоговый", default=1)
    realizing_17 = models.IntegerField(verbose_name="Вес: A(обр)-B(обр) осмысление", default=1)

    temp_18 = models.IntegerField(verbose_name="Вес: -A(обр)-B(обр) промежуточный", default=1)
    correction_18 = models.IntegerField(verbose_name="Вес: Коррекция -A(обр)-B(обр)", default=1)
    result_18 = models.IntegerField(verbose_name="Вес: -A(обр)-B(обр) итоговый", default=1)
    realizing_18 = models.IntegerField(verbose_name="Вес: -A(обр)-B(обр) осмысление", default=1)

    create_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    update_date = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    class Meta:
        verbose_name = "Система оценивания РК2"
        verbose_name_plural = "Системы оценивания РК2"
        get_latest_by = "create_date"


class AnswersBC2(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, verbose_name="Пользователь"
    )

    straight_1 = models.TextField(verbose_name="Прямой код A", default="")
    reversed_1 = models.TextField(verbose_name="Обратный код A", default="")
    additional_1 = models.TextField(verbose_name="Дополнительный код A", default="")
    straight_2 = models.TextField(verbose_name="Прямой код -A", default="")
    reversed_2 = models.TextField(verbose_name="Обратный код -A", default="")
    additional_2 = models.TextField(verbose_name="Дополнительный код -A", default="")
    straight_3 = models.TextField(verbose_name="Прямой код B", default="")
    reversed_3 = models.TextField(verbose_name="Обратный код B", default="")
    additional_3 = models.TextField(verbose_name="Дополнительный код B", default="")
    straight_4 = models.TextField(verbose_name="Прямой код -B", default="")
    reversed_4 = models.TextField(verbose_name="Обратный код -B", default="")
    additional_4 = models.TextField(verbose_name="Дополнительный код -B", default="")
    straight_5 = models.TextField(verbose_name="Прямой код A*2^-n", default="")
    reversed_5 = models.TextField(verbose_name="Обратный код A*2^-n", default="")
    additional_5 = models.TextField(
        verbose_name="Дополнительный код A*2^-n", default=""
    )
    straight_6 = models.TextField(verbose_name="Прямой код A*2^m", default="")
    reversed_6 = models.TextField(verbose_name="Обратный код A*2^m", default="")
    additional_6 = models.TextField(verbose_name="Дополнительный код A*2^m", default="")
    straight_7 = models.TextField(verbose_name="Прямой код A*2^q", default="")
    reversed_7 = models.TextField(verbose_name="Обратный код A*2^q", default="")
    additional_7 = models.TextField(verbose_name="Дополнительный код A*2^q", default="")
    straight_8 = models.TextField(verbose_name="Прямой код B*2^-n", default="")
    reversed_8 = models.TextField(verbose_name="Обратный код B*2^-n", default="")
    additional_8 = models.TextField(
        verbose_name="Дополнительный код B*2^-n", default=""
    )
    straight_9 = models.TextField(verbose_name="Прямой код B*2^m", default="")
    reversed_9 = models.TextField(verbose_name="Обратный код B*2^m", default="")
    additional_9 = models.TextField(verbose_name="Дополнительный код B*2^m", default="")
    straight_10 = models.TextField(verbose_name="Прямой код B*2^q", default="")
    reversed_10 = models.TextField(verbose_name="Обратный код B*2^q", default="")
    additional_10 = models.TextField(
        verbose_name="Дополнительный код B*2^q", default=""
    )

    temp_11 = models.TextField(verbose_name="A(доп) + B(доп) промежуточный", default="")
    correction_11 = models.TextField(
        verbose_name="Коррекция A(доп) + B(доп)", default=""
    )  # 0
    result_11 = models.TextField(verbose_name="A(доп) + B(доп) итоговый", default="")
    realizing_11 = models.TextField(
        verbose_name="A(доп) + B(доп) осмысление", default=""
    )
    temp_12 = models.TextField(
        verbose_name="-A(доп) + B(доп) промежуточный", default=""
    )
    correction_12 = models.TextField(
        verbose_name="Коррекция -A(доп) + B(доп)", default=""
    )  # 0
    result_12 = models.TextField(verbose_name="-A(доп) + B(доп) итоговый", default="")
    realizing_12 = models.TextField(
        verbose_name="-A(доп) + B(доп) осмысление", default=""
    )
    temp_13 = models.TextField(verbose_name="A(доп) - B(доп) промежуточный", default="")
    correction_13 = models.TextField(
        verbose_name="Коррекция A(доп) - B(доп)", default=""
    )  # 1 or 0
    result_13 = models.TextField(verbose_name="A(доп) - B(доп) итоговый", default="")
    realizing_13 = models.TextField(
        verbose_name="A(доп) - B(доп) осмысление", default=""
    )
    temp_14 = models.TextField(
        verbose_name="-A(доп) - B(доп) промежуточный", default=""
    )
    correction_14 = models.TextField(
        verbose_name="Коррекция -A(доп) - B(доп)", default=""
    )  # 1 or 0
    result_14 = models.TextField(verbose_name="-A(доп) - B(доп) итоговый", default="")
    realizing_14 = models.TextField(
        verbose_name="-A(доп) - B(доп) осмысление", default=""
    )

    temp_15 = models.TextField(verbose_name="A(обр) + B(обр) промежуточный", default="")
    correction_15 = models.TextField(
        verbose_name="Коррекция A(обр) + B(обр)", default=""
    )  # 0
    result_15 = models.TextField(verbose_name="A(обр) + B(обр) итоговый", default="")
    realizing_15 = models.TextField(
        verbose_name="A(обр) + B(обр) осмысление", default=""
    )
    temp_16 = models.TextField(
        verbose_name="-A(обр) + B(обр) промежуточный", default=""
    )
    correction_16 = models.TextField(
        verbose_name="Коррекция -A(обр) + B(обр)", default=""
    )  # 0
    result_16 = models.TextField(verbose_name="-A(обр) + B(обр) итоговый", default="")
    realizing_16 = models.TextField(
        verbose_name="-A(обр) + B(обр) осмысление", default=""
    )
    temp_17 = models.TextField(verbose_name="A(обр) - B(обр) промежуточный", default="")
    correction_17 = models.TextField(
        verbose_name="Коррекция A(обр) - B(обр)", default=""
    )  # 1 or 0
    result_17 = models.TextField(verbose_name="A(обр) - B(обр) итоговый", default="")
    realizing_17 = models.TextField(
        verbose_name="A(обр) - B(обр) осмысление", default=""
    )
    temp_18 = models.TextField(
        verbose_name="-A(обр) - B(обр) промежуточный", default=""
    )
    correction_18 = models.TextField(
        verbose_name="Коррекция -A(обр) - B(обр)", default=""
    )  # 1 or 0
    result_18 = models.TextField(verbose_name="-A(обр) - B(обр) итоговый", default="")
    realizing_18 = models.TextField(
        verbose_name="-A(обр) - B(обр) осмысление", default=""
    )

    create_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    update_date = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    class Meta:
        verbose_name = "Ожидаемый ответ"
        verbose_name_plural = "Ожидаемые ответы"
        get_latest_by = "create_date"


class ResultsBC2(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, verbose_name="Пользователь"
    )

    straight_1 = models.TextField(verbose_name="Прямой код A", default="")
    reversed_1 = models.TextField(verbose_name="Обратный код A", default="")
    additional_1 = models.TextField(verbose_name="Дополнительный код A", default="")
    straight_2 = models.TextField(verbose_name="Прямой код B", default="")
    reversed_2 = models.TextField(verbose_name="Обратный код B", default="")
    additional_2 = models.TextField(verbose_name="Дополнительный код B", default="")
    straight_3 = models.TextField(verbose_name="Прямой код -A", default="")
    reversed_3 = models.TextField(verbose_name="Обратный код -A", default="")
    additional_3 = models.TextField(verbose_name="Дополнительный код -A", default="")
    straight_4 = models.TextField(verbose_name="Прямой код -B", default="")
    reversed_4 = models.TextField(verbose_name="Обратный код -B", default="")
    additional_4 = models.TextField(verbose_name="Дополнительный код -B", default="")
    straight_5 = models.TextField(verbose_name="Прямой код A*2^-n", default="")
    reversed_5 = models.TextField(verbose_name="Обратный код A*2^-n", default="")
    additional_5 = models.TextField(
        verbose_name="Дополнительный код A*2^-n", default=""
    )
    straight_6 = models.TextField(verbose_name="Прямой код A*2^m", default="")
    reversed_6 = models.TextField(verbose_name="Обратный код A*2^m", default="")
    additional_6 = models.TextField(verbose_name="Дополнительный код A*2^m", default="")
    straight_7 = models.TextField(verbose_name="Прямой код A*2^q", default="")
    reversed_7 = models.TextField(verbose_name="Обратный код A*2^q", default="")
    additional_7 = models.TextField(verbose_name="Дополнительный код A*2^q", default="")
    straight_8 = models.TextField(verbose_name="Прямой код B*2^-n", default="")
    reversed_8 = models.TextField(verbose_name="Обратный код B*2^-n", default="")
    additional_8 = models.TextField(
        verbose_name="Дополнительный код B*2^-n", default=""
    )
    straight_9 = models.TextField(verbose_name="Прямой код B*2^m", default="")
    reversed_9 = models.TextField(verbose_name="Обратный код B*2^m", default="")
    additional_9 = models.TextField(verbose_name="Дополнительный код B*2^m", default="")
    straight_10 = models.TextField(verbose_name="Прямой код B*2^q", default="")
    reversed_10 = models.TextField(verbose_name="Обратный код B*2^q", default="")
    additional_10 = models.TextField(
        verbose_name="Дополнительный код B*2^q", default=""
    )
    temp_11 = models.TextField(verbose_name="A(доп) + B(доп) промежуточный", default="")
    correction_11 = models.TextField(
        verbose_name="Коррекция A(доп) + B(доп)", default=""
    )  # 0
    result_11 = models.TextField(verbose_name="A(доп) + B(доп) итоговый", default="")
    realizing_11 = models.TextField(
        verbose_name="A(доп) + B(доп) осмысление", default=""
    )
    temp_12 = models.TextField(
        verbose_name="-A(доп) + B(доп) промежуточный", default=""
    )
    correction_12 = models.TextField(
        verbose_name="Коррекция -A(доп) + B(доп)", default=""
    )  # 0
    result_12 = models.TextField(verbose_name="-A(доп) + B(доп) итоговый", default="")
    realizing_12 = models.TextField(
        verbose_name="-A(доп) + B(доп) осмысление", default=""
    )
    temp_13 = models.TextField(verbose_name="A(доп) - B(доп) промежуточный", default="")
    correction_13 = models.TextField(
        verbose_name="Коррекция A(доп) - B(доп)", default=""
    )  # 1 or 0
    result_13 = models.TextField(verbose_name="A(доп) - B(доп) итоговый", default="")
    realizing_13 = models.TextField(
        verbose_name="A(доп) - B(доп) осмысление", default=""
    )
    temp_14 = models.TextField(
        verbose_name="-A(доп) - B(доп) промежуточный", default=""
    )
    correction_14 = models.TextField(
        verbose_name="Коррекция -A(доп) - B(доп)", default=""
    )  # 1 or 0
    result_14 = models.TextField(verbose_name="-A(доп) - B(доп) итоговый", default="")
    realizing_14 = models.TextField(
        verbose_name="-A(доп) - B(доп) осмысление", default=""
    )

    temp_15 = models.TextField(verbose_name="A(обр) + B(обр) промежуточный", default="")
    correction_15 = models.TextField(
        verbose_name="Коррекция A(обр) + B(обр)", default=""
    )  # 0
    result_15 = models.TextField(verbose_name="A(обр) + B(обр) итоговый", default="")
    realizing_15 = models.TextField(
        verbose_name="A(обр) + B(обр) осмысление", default=""
    )
    temp_16 = models.TextField(
        verbose_name="-A(обр) + B(обр) промежуточный", default=""
    )
    correction_16 = models.TextField(
        verbose_name="Коррекция -A(обр) + B(обр)", default=""
    )  # 0
    result_16 = models.TextField(verbose_name="-A(обр) + B(обр) итоговый", default="")
    realizing_16 = models.TextField(
        verbose_name="-A(обр) + B(обр) осмысление", default=""
    )
    temp_17 = models.TextField(verbose_name="A(обр) - B(обр) промежуточный", default="")
    correction_17 = models.TextField(
        verbose_name="Коррекция A(обр) - B(обр)", default=""
    )  # 1 or 0
    result_17 = models.TextField(verbose_name="A(обр) - B(обр) итоговый", default="")
    realizing_17 = models.TextField(
        verbose_name="A(обр) - B(обр) осмысление", default=""
    )
    temp_18 = models.TextField(
        verbose_name="-A(обр) - B(обр) промежуточный", default=""
    )
    correction_18 = models.TextField(
        verbose_name="Коррекция -A(обр) - B(обр)", default=""
    )  # 1 or 0
    result_18 = models.TextField(verbose_name="-A(обр) - B(обр) итоговый", default="")
    realizing_18 = models.TextField(
        verbose_name="-A(обр) - B(обр) осмысление", default=""
    )

    create_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    update_date = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    class Meta:
        verbose_name = "Пользовательский ответ"
        verbose_name_plural = "Пользовательские ответы"
        get_latest_by = "create_date"


# Create your models here.
class BorderControl2(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, verbose_name="Пользователь"
    )
    number1 = models.IntegerField(blank=False, verbose_name="Число 1", default="3")
    number2 = models.IntegerField(blank=False, verbose_name="Число 2", default="-13")
    degree_1 = models.IntegerField(blank=False, verbose_name="Степень 1", default="2")
    degree_2 = models.IntegerField(blank=False, verbose_name="Степень 2", default="-2")
    degree_3 = models.IntegerField(blank=False, verbose_name="Степень 3", default="3")
    answers = models.ForeignKey(
        "AnswersBC2", on_delete=models.CASCADE, verbose_name="Ожидаемые ответы"
    )
    results = models.ForeignKey(
        "ResultsBC2",
        on_delete=models.CASCADE,
        verbose_name="Пользовательские ответы",
        blank=True,
        null=True,
    )
    result_number = models.IntegerField(verbose_name="Оценка", default=0)
    rating = models.IntegerField(
        default=0,
        null=False,
        validators=[MinValueValidator(0), MaxValueValidator(50)],
        verbose_name="Баллы",
    )

    create_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    update_date = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    class Meta:
        verbose_name = "РК номер 2"
        verbose_name_plural = "РК номер 2"
        get_latest_by = "create_date"
