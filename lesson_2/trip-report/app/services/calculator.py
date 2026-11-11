def calculate_total(expenses):
    total = 0
    for expense in expenses:
        total += expense["amount"]
    return total


def calculate_average(expenses):
    if not expenses:
        raise ValueError("список расходов пуст")
    return calculate_total(expenses) / len(expenses)


def most_expensive_day(expenses):
    if not expenses:
        raise ValueError("пусто")
    days = {}
    for num in expenses:
        days[num["day"]] = days.get(num["day"], 0) + num["amount"]
    max_num = max(days, key=days.get)
    return max_num, days[max_num]

def category_share(expenses, category):
    if not expenses:
        raise ValueError("пусто")
    total = calculate_total(expenses)
    part = sum(num["amount"] for num in expenses if num["category"] == category)
    if part == 0:
        raise ValueError("нет категории")
    return part / total * 100

