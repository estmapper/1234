import random

from border_control2.models import AnswersBC2, BorderControl2, ResultsBC2, RatingBC2


def convert_straight(number: int):
    number = int(number)
    if number > 127 or number < -128:
        return "-"
    string = ""
    neg = number < 0
    if number == 0:
        return "0.0000000"
    number = abs(number)
    while number > 0:
        string = str(number % 2) + string
        number //= 2

    while len(string) < 7:
        string = "0" + string

    if neg:
        string = "1." + string
    else:
        string = "0." + string
    return string


def convert_reversed(number: int):
    number = int(number)
    if number > 127 or number < -128:
        return "-"
    if number >= 0:
        return convert_straight(number)
    string = ""
    number = abs(number)
    while number > 0:
        temp = str(number % 2)
        if temp == "0":
            string = "1" + string
        if temp == "1":
            string = "0" + string
        number //= 2

    while len(string) < 7:
        string = "1" + string

    string = "1." + string
    return string


def convert_addition(number: int):
    number = int(number)
    if number > 127 or number < -128:
        return "-"
    if number >= 0:
        return convert_straight(number)
    string = convert_reversed(number)
    answer = ""
    flag = True
    length = len(convert_reversed(number))
    for i in range(length - 1, -1, -1):
        if flag:
            if string[i] == "1":
                answer = "0" + answer
            elif string[i] == "0":
                flag = False
                answer = "1" + answer
        else:
            answer = string[i] + answer
    return answer


def binary_sum(num1, num2):
    # split the numbers into integer and fractional parts
    int_part1, frac_part1 = num1.split(".")
    int_part2, frac_part2 = num2.split(".")

    # make fractional parts of equal length by padding with zeros
    max_frac_length = max(len(frac_part1), len(frac_part2))
    frac_part1 = frac_part1.ljust(max_frac_length, "0")
    frac_part2 = frac_part2.ljust(max_frac_length, "0")

    # add fractional parts
    frac_sum = ""
    carry = 0
    for i in range(max_frac_length - 1, -1, -1):
        bit_sum = int(frac_part1[i]) + int(frac_part2[i]) + carry
        frac_sum = str(bit_sum % 2) + frac_sum
        carry = bit_sum // 2

    # add integer parts
    int_sum = ""
    max_int_length = max(len(int_part1), len(int_part2))
    int_part1 = int_part1.zfill(max_int_length)
    int_part2 = int_part2.zfill(max_int_length)

    for i in range(max_int_length - 1, -1, -1):
        bit_sum = int(int_part1[i]) + int(int_part2[i]) + carry
        int_sum = str(bit_sum % 2) + int_sum
        carry = bit_sum // 2

    # if there is still a carry left, add it to the integer part
    if carry:
        int_sum = "1" + int_sum

    return int_sum + "." + frac_sum


def sum_numbers(number1, number2):
    num1 = convert_reversed(number1)
    num2 = convert_reversed(number2)

    result = binary_sum(num1, num2)

    return result


def correction(number):
    if len(number) < 10:
        return "-"
    else:
        return number[0]


def create_control(user) -> BorderControl2:
    number1 = random.randint(5, 64)
    number2 = random.randint(-10, -1)

    degree_1 = random.randint(-3, -2)
    degree_2 = random.randint(2, 3)
    degree_3 = random.randint(2, 4)

    while degree_2 == degree_3:
        degree_3 = random.randint(2, 4)

    while number1 == number2:
        number2 = random.randint(-5, 75)

    control = BorderControl2.objects.create(
        user=user,
        number1=number1,
        number2=number2,
        degree_1=degree_1,
        degree_2=degree_2,
        degree_3=degree_3,
        answers=make_answers(user, number1, number2, degree_1, degree_2, degree_3),
    )

    return control


def validity(answers: AnswersBC2, results: ResultsBC2):
    counter = 0
    rating = RatingBC2.objects.filter(is_active=True).first()

    if (
        answers.straight_1 == results.straight_1
        and answers.reversed_1 == results.reversed_1
        and answers.additional_1 == results.additional_1
    ):
        counter += rating.a

    if (
        answers.straight_2 == results.straight_2
        and answers.reversed_2 == results.reversed_2
        and answers.additional_2 == results.additional_2
    ):
        counter += rating.minus_a

    if (
        answers.straight_3 == results.straight_3
        and answers.reversed_3 == results.reversed_3
        and answers.additional_3 == results.additional_3
    ):
        counter += rating.b

    if (
        answers.straight_4 == results.straight_4
        and answers.reversed_4 == results.reversed_4
        and answers.additional_4 == results.additional_4
    ):
        counter += rating.minus_b

    if (
        answers.straight_5 == results.straight_5
        and answers.reversed_5 == results.reversed_5
        and answers.additional_5 == results.additional_5
    ):
        counter += rating.a_n

    if (
        answers.straight_6 == results.straight_6
        and answers.reversed_6 == results.reversed_6
        and answers.additional_6 == results.additional_6
    ):
        counter += rating.a_m

    if (
        answers.straight_7 == results.straight_7
        and answers.reversed_7 == results.reversed_7
        and answers.additional_7 == results.additional_7
    ):
        counter += rating.a_q

    if (
        answers.straight_8 == results.straight_8
        and answers.reversed_8 == results.reversed_8
        and answers.additional_8 == results.additional_8
    ):
        counter += rating.b_n

    if (
        answers.straight_9 == results.straight_9
        and answers.reversed_9 == results.reversed_9
        and answers.additional_9 == results.additional_9
    ):
        counter += rating.b_m

    if (
        answers.straight_10 == results.straight_10
        and answers.reversed_10 == results.reversed_10
        and answers.additional_10 == results.additional_10
    ):
        counter += rating.b_q

    if (
        answers.temp_11 == results.temp_11
        and answers.correction_11 == results.correction_11
        and answers.result_11 == results.result_11
        and answers.realizing_11 == results.realizing_11
    ):
        counter += rating.a_b_add

    if (
        answers.temp_12 == results.temp_12
        and answers.correction_12 == results.correction_12
        and answers.result_12 == results.result_12
        and answers.realizing_12 == results.realizing_12
    ):
        counter += rating.minus_a_b_add

    if (
        answers.temp_13 == results.temp_13
        and answers.correction_13 == results.correction_13
        and answers.result_13 == results.result_13
        and answers.realizing_13 == results.realizing_13
    ):
        counter += rating.a_minus_b_add

    if (
        answers.temp_14 == results.temp_14
        and answers.correction_14 == results.correc4ion_13
        and answers.result_14 == results.result_14
        and answers.realizing_14 == results.realizing_14
    ):
        counter += rating.minus_a_minus_b_add

    if (
        answers.temp_15 == results.temp_15
        and answers.correction_15 == results.correction_15
        and answers.result_15 == results.result_15
        and answers.realizing_15 == results.realizing_15
    ):
        counter += rating.a_b_rev

    if (
        answers.temp_16 == results.temp_16
        and answers.correction_16 == results.correction_16
        and answers.result_16 == results.result_16
        and answers.realizing_16 == results.realizing_16
    ):
        counter += rating.minus_a_b_rev

    if (
        answers.temp_17 == results.temp_17
        and answers.correction_17 == results.correction_17
        and answers.result_17 == results.result_17
        and answers.realizing_17 == results.realizing_17
    ):
        counter += rating.a_minus_b_rev

    if (
        answers.temp_18 == results.temp_18
        and answers.correction_18 == results.correction_18
        and answers.result_18 == results.result_18
        and answers.realizing_18 == results.realizing_18
    ):
        counter += rating.minus_a_minus_b_rev

    return counter


def get_results_and_rating(answers: AnswersBC2, results: ResultsBC2):
    # Per-field weighted scoring using latest active RatingBC2
    try:
        rating_obj = RatingBC2.objects.filter(is_active=True).latest()
    except Exception:
        rating_obj = None

    def w(name):
        return getattr(rating_obj, name, 1) if rating_obj else 1

    checks = []  # (is_correct, weight_name)

    # A, -A, B, -B
    checks.append((answers.straight_1 == results.straight_1, "straight_1"))
    checks.append((answers.reversed_1 == results.reversed_1, "reversed_1"))
    checks.append((answers.additional_1 == results.additional_1, "additional_1"))

    checks.append((answers.straight_2 == results.straight_2, "straight_2"))
    checks.append((answers.reversed_2 == results.reversed_2, "reversed_2"))
    checks.append((answers.additional_2 == results.additional_2, "additional_2"))

    checks.append((answers.straight_3 == results.straight_3, "straight_3"))
    checks.append((answers.reversed_3 == results.reversed_3, "reversed_3"))
    checks.append((answers.additional_3 == results.additional_3, "additional_3"))

    checks.append((answers.straight_4 == results.straight_4, "straight_4"))
    checks.append((answers.reversed_4 == results.reversed_4, "reversed_4"))
    checks.append((answers.additional_4 == results.additional_4, "additional_4"))

    # Degree variants
    checks.append((answers.straight_5 == results.straight_5, "straight_5"))
    checks.append((answers.reversed_5 == results.reversed_5, "reversed_5"))
    checks.append((answers.additional_5 == results.additional_5, "additional_5"))

    checks.append((answers.straight_6 == results.straight_6, "straight_6"))
    checks.append((answers.reversed_6 == results.reversed_6, "reversed_6"))
    checks.append((answers.additional_6 == results.additional_6, "additional_6"))

    checks.append((answers.straight_7 == results.straight_7, "straight_7"))
    checks.append((answers.reversed_7 == results.reversed_7, "reversed_7"))
    checks.append((answers.additional_7 == results.additional_7, "additional_7"))

    checks.append((answers.straight_8 == results.straight_8, "straight_8"))
    checks.append((answers.reversed_8 == results.reversed_8, "reversed_8"))
    checks.append((answers.additional_8 == results.additional_8, "additional_8"))

    checks.append((answers.straight_9 == results.straight_9, "straight_9"))
    checks.append((answers.reversed_9 == results.reversed_9, "reversed_9"))
    checks.append((answers.additional_9 == results.additional_9, "additional_9"))

    checks.append((answers.straight_10 == results.straight_10, "straight_10"))
    checks.append((answers.reversed_10 == results.reversed_10, "reversed_10"))
    checks.append((answers.additional_10 == results.additional_10, "additional_10"))

    # Additional code ops (11-14)
    checks.append((answers.temp_11 == results.temp_11, "temp_11"))
    checks.append((answers.correction_11 == results.correction_11, "correction_11"))
    checks.append((answers.result_11 == results.result_11, "result_11"))
    checks.append((answers.realizing_11 == results.realizing_11, "realizing_11"))

    checks.append((answers.temp_12 == results.temp_12, "temp_12"))
    checks.append((answers.correction_12 == results.correction_12, "correction_12"))
    checks.append((answers.result_12 == results.result_12, "result_12"))
    checks.append((answers.realizing_12 == results.realizing_12, "realizing_12"))

    checks.append((answers.temp_13 == results.temp_13, "temp_13"))
    checks.append((answers.correction_13 == results.correction_13, "correction_13"))
    checks.append((answers.result_13 == results.result_13, "result_13"))
    checks.append((answers.realizing_13 == results.realizing_13, "realizing_13"))

    checks.append((answers.temp_14 == results.temp_14, "temp_14"))
    checks.append((answers.correction_14 == results.correction_14, "correction_14"))
    checks.append((answers.result_14 == results.result_14, "result_14"))
    checks.append((answers.realizing_14 == results.realizing_14, "realizing_14"))

    # Reverse code ops (15-18)
    checks.append((answers.temp_15 == results.temp_15, "temp_15"))
    checks.append((answers.correction_15 == results.correction_15, "correction_15"))
    checks.append((answers.result_15 == results.result_15, "result_15"))
    checks.append((answers.realizing_15 == results.realizing_15, "realizing_15"))

    checks.append((answers.temp_16 == results.temp_16, "temp_16"))
    checks.append((answers.correction_16 == results.correction_16, "correction_16"))
    checks.append((answers.result_16 == results.result_16, "result_16"))
    checks.append((answers.realizing_16 == results.realizing_16, "realizing_16"))

    checks.append((answers.temp_17 == results.temp_17, "temp_17"))
    checks.append((answers.correction_17 == results.correction_17, "correction_17"))
    checks.append((answers.result_17 == results.result_17, "result_17"))
    checks.append((answers.realizing_17 == results.realizing_17, "realizing_17"))

    checks.append((answers.temp_18 == results.temp_18, "temp_18"))
    checks.append((answers.correction_18 == results.correction_18, "correction_18"))
    checks.append((answers.result_18 == results.result_18, "result_18"))
    checks.append((answers.realizing_18 == results.realizing_18, "realizing_18"))

    max_weight = sum(wname and w(wname) for _, wname in checks)
    gained_weight = sum(w(wname) for ok, wname in checks if ok)

    if max_weight <= 0:
        return 0, 0

    proportion = gained_weight / max_weight
    result_number = int(round(proportion * 10))

    return int(gained_weight), result_number


def make_answers(user, number1, number2, degree_1, degree_2, degree_3):
    answers = AnswersBC2.objects.create(
        user=user,
        # table A B -A -B
        # A
        straight_1=convert_straight(number1),
        reversed_1=convert_reversed(number1),
        additional_1=convert_addition(number1),
        # -A
        straight_2=convert_straight(-number1),
        reversed_2=convert_reversed(-number1),
        additional_2=convert_addition(-number1),
        # B
        straight_3=convert_straight(number2),
        reversed_3=convert_reversed(number2),
        additional_3=convert_addition(number2),
        # -B
        straight_4=convert_straight(-number2),
        reversed_4=convert_reversed(-number2),
        additional_4=convert_addition(-number2),
        # A * deg1
        straight_5=convert_straight(number1 * (2**degree_1)),
        reversed_5=convert_reversed(number1 * (2**degree_1)),
        additional_5=convert_addition(number1 * (2**degree_1)),
        # A * deg2
        straight_6=convert_straight(number1 * (2**degree_2)),
        reversed_6=convert_reversed(number1 * (2**degree_2)),
        additional_6=convert_addition(number1 * (2**degree_2)),
        # A * deg3
        straight_7=convert_straight(number1 * (2**degree_3)),
        reversed_7=convert_reversed(number1 * (2**degree_3)),
        additional_7=convert_addition(number1 * (2**degree_3)),
        # B * deg1
        straight_8=convert_straight(number2 * (2**degree_1)),
        reversed_8=convert_reversed(number2 * (2**degree_1)),
        additional_8=convert_addition(number2 * (2**degree_1)),
        # B * deg2
        straight_9=convert_straight(number2 * (2**degree_2)),
        reversed_9=convert_reversed(number2 * (2**degree_2)),
        additional_9=convert_addition(number2 * (2**degree_2)),
        # B * deg3
        straight_10=convert_straight(number2 * (2**degree_3)),
        reversed_10=convert_reversed(number2 * (2**degree_3)),
        additional_10=convert_addition(number2 * (2**degree_3)),
        # Aд + Вд
        temp_11=convert_addition(number1 + number2),
        correction_11="0",
        result_11=convert_addition(number1 + number2),
        realizing_11=convert_straight(number1 + number2),
        # -Ад + Вд
        temp_12=convert_addition(-number1 + number2),
        correction_12="0",
        result_12=convert_addition(-number1 + number2),
        realizing_12=convert_straight(-number1 + number2),
        # Ад - Вд
        temp_13=convert_addition(number1 - number2),
        correction_13="0",
        result_13=convert_addition(number1 - number2),
        realizing_13=convert_straight(number1 - number2),
        # -Ад - Вд
        temp_14=sum_numbers(-number1, -number2),
        correction_14="0",
        result_14=convert_reversed(-number1 - number2),
        realizing_14=convert_straight(-number1 - number2),
        # Aо + Во
        temp_15=sum_numbers(number1, number2),
        correction_15=correction(sum_numbers(number1, number2)),
        result_15=convert_reversed(number1 + number2),
        realizing_15=convert_straight(number1 + number2),
        # -Ао + Во
        temp_16=sum_numbers(-number1, number2),
        correction_16=correction(sum_numbers(-number1, number2)),
        result_16=convert_reversed(-number1 + number2),
        realizing_16=convert_straight(-number1 + number2),
        # Ао - Во
        temp_17=sum_numbers(number1, -number2),
        correction_17=correction(sum_numbers(number1, -number2)),
        result_17=convert_reversed(number1 - number2),
        realizing_17=convert_straight(number1 - number2),
        # -Ао - Во
        temp_18=sum_numbers(-number1, -number2),
        correction_18=correction(sum_numbers(-number1, -number2)),
        result_18=convert_reversed(-number1 - number2),
        realizing_18=convert_straight(-number1 - number2),
    )
    return answers
