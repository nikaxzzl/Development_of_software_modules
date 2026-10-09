from app.services.calculator import (
    calculate_total,
    calculate_average,
    most_expensive_day,
    category_share,
)


def print_report(expenses):
    total = calculate_total(expenses)
    average = calculate_average(expenses)
    day, day_sum = most_expensive_day(expenses)

    lines = [
        "ОТЧЁТ ПО ПОЕЗДКЕ",
        f"всего потрачено: {total} ₽",
        f"средняя трата: {average:} ₽",
        f"самый дорогой день: день {day}, {day_sum} ₽",
        f"доля «еда»: {category_share(expenses, 'еда'):.2f} %",
        f"доля «жильё»: {category_share(expenses, 'жильё'):.2f} %",
    ]
    print("\n".join(lines))