def format_average(value: float) -> str:
    return f"Средний результат: {value:.2f}"


def format_report(average: float, min_v: int, max_v: int) -> str:
    return (
        f"Средний результат: {average:.2f}\n"
        f"Минимальная оценка: {min_v}\n"
        f"Максимальная оценка: {max_v}"
    )