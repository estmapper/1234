import random

from border_control1.models import AnswersBC1, BorderControl1, ResultsBC1, RatingBC1


def convert_integer_part(n, base):
    """Конвертирует целую часть числа в указанную систему счисления"""
    if n == 0:
        return "0"
    digits = []
    n = int(n)
    while n > 0:
        remainder = n % base
        # Используем только цифры 0-9 и буквы A-F
        digits.append(
            str(remainder) if remainder < 10 else chr(ord("A") + remainder - 10)
        )
        n = n // base
    return "".join(reversed(digits))


def convert_fractional_part(fraction, base, precision=8):
    fraction = fraction/1000
    """Конвертирует дробную часть числа в указанную систему счисления"""
    if fraction == 0:
        return ""

    digits = []
    for _ in range(precision):
        fraction *= base
        digit = int(fraction)
        # Используем только цифры 0-9 и буквы A-F
        digits.append(str(digit) if digit < 10 else chr(ord("A") + digit - 10))
        fraction -= digit
        if fraction < 1e-10:  # Условие выхода при достижении нуля
            break

    return "".join(digits)


def create_control(user) -> BorderControl1:

    number = round(random.uniform(100.001, 999.999), 3)
    number_sec = random.randint(100, 999)
    number_trd = random.randint(100, 999)
    number_fth = random.randint(100,999)
    p_index = random.randint(0, 2)
    p_system = [3, 5, 7][p_index]
    number_main = int(number)
    number_add = int((number * 1000) % 1000)
    control = BorderControl1.objects.create(
        user=user,
        number=number,
        number_sec = number_sec,
        number_trd = number_trd,
        number_fth = number_fth,
        p_system=p_system,
        answers=make_answers(user, number,number_sec, number_trd, number_fth, number_main, number_add, p_system),
    )

    return control


def validity(answers: AnswersBC1, results: ResultsBC1):
    counter = 0
    # подумать какие тут коэффициенты должны быть
    if answers.float_bin == results.float_bin:
        counter += 1
    if answers.float_oct == results.float_oct:
        counter += 1
    if answers.float_hex == results.float_hex:
        counter += 1
    if answers.int_bin == results.int_bin:
        counter += 1
    if answers.int_oct == results.int_oct:
        counter += 1
    if answers.int_hex == results.int_hex:
        counter += 1
    if answers.int_sec_p == results.int_sec_p:
        counter += 1
    if answers.int_sec_bin == results.int_sec_bin:
        counter += 1
    if answers.int_trd == results.int_trd:
        counter += 1
    if answers.int_trd_p == results.int_trd_p:
        counter += 1
    if answers.int_fth == results.int_fth:
        counter += 1
    if answers.int_fth_bin == results.int_fth_bin:
        counter += 1
    return counter


def get_results_and_rating(answers: AnswersBC1, results: ResultsBC1):
    # Load latest active rating system; fallback to equal weights if none
    try:
        rating_cfg = RatingBC1.objects.filter(is_active=True).latest()
    except Exception:
        rating_cfg = None

    # Build a list of (is_correct, weight)
    checks = []
    def w(name):
        if rating_cfg is None:
            return 1
        return getattr(rating_cfg, name, 1)

    checks.append((answers.float_bin == results.float_bin, w("float_bin")))
    checks.append((answers.float_oct == results.float_oct, w("float_oct")))
    checks.append((answers.float_hex == results.float_hex, w("float_hex")))
    checks.append((answers.int_bin == results.int_bin, w("int_bin")))
    checks.append((answers.int_oct == results.int_oct, w("int_oct")))
    checks.append((answers.int_hex == results.int_hex, w("int_hex")))
    checks.append((answers.int_sec_p == results.int_sec_p, w("int_sec_p")))
    checks.append((answers.int_sec_bin == results.int_sec_bin, w("int_sec_bin")))
    checks.append((answers.int_trd == results.int_trd, w("int_trd")))
    checks.append((answers.int_trd_p == results.int_trd_p, w("int_trd_p")))
    checks.append((answers.int_fth == results.int_fth, w("int_fth")))
    checks.append((answers.int_fth_bin == results.int_fth_bin, w("int_fth_bin")))

    total_weight = sum(weight for _, weight in checks)
    gained_weight = sum(weight for ok, weight in checks if ok)

    # rating: total weighted points obtained
    rating = gained_weight

    # result_number: map proportion to {0,2,4,6,8,10}
    if total_weight <= 0:
        result_number = 0
    else:
        proportion = gained_weight / total_weight
        result_number = int(round(proportion * 5)) * 2

    return int(rating), result_number


def make_answers(user, number, number_sec,number_trd,number_fth, number_main, number_add, p_system):
    answers = AnswersBC1.objects.create(
        user=user,
        float_bin=convert_fractional_part(number_add, 2, 9),
        float_oct=convert_fractional_part(number_add, 8, 3),
        float_hex=convert_fractional_part(number_add, 16, 2),
        int_bin=convert_integer_part(number_main, 2),
        int_oct=convert_integer_part(number_main, 8),
        int_hex=convert_integer_part(number_main, 16),
        int_sec_bin=convert_integer_part(number_sec, 2),
        int_sec_p=convert_integer_part(number_sec, p_system),
        int_trd=convert_integer_part(number_trd, 10),
        int_trd_p=convert_integer_part(number_trd, p_system),
        int_fth=convert_integer_part(number_fth, 10),
        int_fth_bin=convert_integer_part(number_fth, 2),
    )
    return answers
