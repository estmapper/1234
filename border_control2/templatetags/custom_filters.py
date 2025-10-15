from django import template

register = template.Library()


@register.filter
def getattr(obj, attr_prefix):
    def _getattr(obj, attr):
        if hasattr(obj, attr):
            return getattr(obj, attr)
        return ""

    attr_name = f"{attr_prefix}{obj}"
    return _getattr(obj, attr_name) if isinstance(obj, object) else ""


@register.filter(is_safe=True)
def compare_chars(user_answer, correct_answer):
    """
    Возвращает HTML с подсветкой символов: зелёный — совпадает, красный — нет.
    Если длины строк не равны, все символы подсвечиваются красным.
    """
    if not user_answer or not correct_answer:
        return ""

    user_str = str(user_answer)
    correct_str = str(correct_answer)

    # Если длины не равны, подсвечиваем все красным
    if len(user_str) != len(correct_str):
        result = ""
        for u in user_str:
            result += f'<span class="incorrect-char">{u}</span>'
        return result

    # Если длины равны, сравниваем посимвольно
    result = ""
    for u, c in zip(user_str, correct_str):
        if u == c:
            result += f'<span class="correct-char">{u}</span>'
        else:
            result += f'<span class="incorrect-char">{u}</span>'

    return result
