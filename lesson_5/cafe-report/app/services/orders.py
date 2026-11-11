"""Заказы: чтение из файла и расчёты по ним."""

import csv
from pathlib import Path
from typing import TypedDict

from app.utils.text import normalize_name


class Order(TypedDict):
    waiter: str
    kopeks: int


def load_orders(path: Path) -> list[Order]:
    """Читает заказы из CSV-файла: официант и сумма заказа в копейках.

    Имена в файле записаны по-разному, поэтому здесь они сразу приводятся
    к одному виду: дальше по ним можно группировать заказы.
    """
    with open(path, encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        return [
            Order(
                waiter=normalize_name(row["waiter"]),
                kopeks=int(row["kopeks"]),
            )
            for row in reader
        ]


def total_kopeks(orders: list[Order]) -> int:
    """Считает выручку по всем заказам в копейках."""
    return sum(order["kopeks"] for order in orders)


def average_kopeks(orders: list[Order]) -> float:
    """Считает средний чек в копейках. Для пустого списка вызывает ValueError."""
    if not orders:
        raise ValueError("Список заказов пуст")
    return total_kopeks(orders) / len(orders)


def kopeks_by_waiter(orders: list[Order]) -> dict[str, int]:
    """Складывает суммы заказов по каждому официанту."""
    result: dict[str, int] = {}
    for order in orders:
        waiter = order["waiter"]
        result[waiter] = result.get(waiter, 0) + order["kopeks"]
    return result