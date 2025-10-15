import uuid
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from automata_theory.models import CustomUser, KRTime


class RatingBC1(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    is_active = models.BooleanField(verbose_name="Активная система оценивания", default=True)

    float_bin = models.IntegerField(verbose_name="A frac (bin)", default=1)
    float_oct = models.IntegerField(verbose_name="A frac (oct)", default=1)
    float_hex = models.IntegerField(verbose_name="A frac (hex)", default=1)

    int_bin = models.IntegerField(verbose_name="A int (bin)", default=1)
    int_oct = models.IntegerField(verbose_name="A int (oct)", default=1)
    int_hex = models.IntegerField(verbose_name="A int (hex)", default=1)

    int_sec_bin = models.IntegerField(verbose_name="B int (bin)", default=1)
    int_sec_p = models.IntegerField(verbose_name="B int (p)", default=1)

    int_trd = models.IntegerField(verbose_name="C int (dec)", default=1)
    int_trd_p = models.IntegerField(verbose_name="C int (p)", default=1)

    int_fth = models.IntegerField(verbose_name="D int (dec)", default=1)
    int_fth_bin = models.IntegerField(verbose_name="D int (bin)", default=1)

    create_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    update_date = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    class Meta:
        verbose_name = "Система оценивания РК1"
        verbose_name_plural = "Системы оценивания РК1"
        get_latest_by = "create_date"


class AnswersBC1(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, verbose_name="Пользователь"
    )

    float_bin = models.TextField(
        verbose_name="Вещественная часть числа А в 2 сс", default=""
    )
    float_oct = models.TextField(
        verbose_name="Вещественная часть числа А в 8 сс", default=""
    )
    float_hex = models.TextField(
        verbose_name="Вещественная часть числа А в 16 сс", default=""
    )
    int_bin = models.TextField(
        verbose_name="Целочисленная часть числа А в 2 сс", default=""
    )
    int_oct = models.TextField(
        verbose_name="Целочисленная часть числа А в 8 сс", default=""
    )
    int_hex = models.TextField(
        verbose_name="Целочисленная часть числа А в 16 сс", default=""
    )
    int_sec_bin = models.TextField(
        verbose_name="Целочисленная часть числа B в 2 сс", default=""
    )
    int_sec_p = models.TextField(
        verbose_name="Целочисленная часть числа B в p сс", default=""
    )
    int_trd = models.TextField(
        verbose_name="Целочисленная часть числа C в 10 сс", default=""
    )
    int_trd_p = models.TextField(
        verbose_name="Целочисленная часть числа C в p сс", default=""
    )
    int_fth = models.TextField(
        verbose_name="Целочисленная часть числа D в 10 сс", default=""
    )
    int_fth_bin = models.TextField(
        verbose_name="Целочисленная часть числа D в 2 сс", default=""
    )

    create_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    update_date = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    class Meta:
        verbose_name = "Ожидаемый ответ"
        verbose_name_plural = "Ожидаемые ответы"
        get_latest_by = "create_date"


class ResultsBC1(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, verbose_name="Пользователь"
    )

    float_bin = models.TextField(
        verbose_name="Вещественная часть числа А в 2 сс", default=""
    )
    float_oct = models.TextField(
        verbose_name="Вещественная часть числа А в 8 сс", default=""
    )
    float_hex = models.TextField(
        verbose_name="Вещественная часть числа А в 16 сс", default=""
    )
    int_bin = models.TextField(
        verbose_name="Целочисленная часть числа А в 2 сс", default=""
    )
    int_oct = models.TextField(
        verbose_name="Целочисленная часть числа А в 8 сс", default=""
    )
    int_hex = models.TextField(
        verbose_name="Целочисленная часть числа А в 16 сс", default=""
    )
    int_sec_bin = models.TextField(
        verbose_name="Целочисленная часть числа B в 2 сс", default=""
    )
    int_sec_p = models.TextField(
        verbose_name="Целочисленная часть числа B в p сс", default=""
    )
    int_trd = models.TextField(
        verbose_name="Целочисленная часть числа C в 10 сс", default=""
    )
    int_trd_p = models.TextField(
        verbose_name="Целочисленная часть числа C в p сс", default=""
    )
    int_fth = models.TextField(
        verbose_name="Целочисленная часть числа D в 10 сс", default=""
    )
    int_fth_bin = models.TextField(
        verbose_name="Целочисленная часть числа D в 2 сс", default=""
    )

    create_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    update_date = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    class Meta:
        verbose_name = "Пользовательский ответ"
        verbose_name_plural = "Пользовательские ответы"
        get_latest_by = "create_date"


class BorderControl1(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, verbose_name="Пользователь"
    )
    number = models.FloatField(
        verbose_name="Число A в десятичной системе счисления", default=1
    )
    number_sec = models.IntegerField(
        verbose_name="Число B в десятичной системе счисления", default=1
    )
    number_trd = models.IntegerField(
        verbose_name="Число C в десятичной системе счисления", default=1
    )
    number_fth = models.IntegerField(verbose_name="Число D в десятичной системе счисленияс", default=30)
    p_system = models.IntegerField(verbose_name="Система счисления P", default=8)

    answers = models.ForeignKey(
        "AnswersBC1", on_delete=models.CASCADE, verbose_name="Ожидаемые ответы"
    )
    results = models.ForeignKey(
        "ResultsBC1",
        on_delete=models.CASCADE,
        verbose_name="Пользовательские ответы",
        blank=True,
        null=True,
    )
    result_number = models.IntegerField(verbose_name="Оценка", default=0)
    rating = models.IntegerField(
        default=0,
        null=False,
        validators=[MinValueValidator(0), MaxValueValidator(38)],
        verbose_name="Баллы",
    )

    create_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    update_date = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    class Meta:
        verbose_name = "РК номер 1"
        verbose_name_plural = "РК номер 1"
        get_latest_by = "create_date"
