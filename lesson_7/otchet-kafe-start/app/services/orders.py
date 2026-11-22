"""Загрузка, сортировка и подсчёт выручки по заказам."""
from pathlib import Path

from app.domain.order import Order
from app.services.importer import read_rows


def load_orders(path: Path) -> list[Order]:
    """Загружает заказы из файла CSV.
    
    Args:
        path: Путь к CSV-файлу со списком заказов.
    
    Returns:
        Список объектов Order, прочитанных из файла.
    """    
    return [
        Order(waiter=row["waiter"], kopeks=int(row["kopeks"]))
        for row in read_rows(path)
    ]


def revenue_by_waiter(orders: list[Order], top: int = 0) -> dict[str, int]:
    """Считает выручку по каждому официанту.

    Args:
        orders: Заказы за смену, список не должен быть пустым.
        top: Сколько официантов оставить в итоге. Число 0 значит,что возвращаются все.

    Returns:
        Выручка в копейках по именам официантов, в порядке убывания суммы.

    Raises:
        ValueError: Если список заказов пуст.
    """        
    if not orders:
        raise ValueError("Список заказов пуст")
    totals: dict[str, int] = {}
    for order in orders:
        totals[order.waiter] = totals.get(order.waiter, 0) + order.kopeks
    ranked = sorted(totals.items(), key=lambda pair: -pair[1])
    if top:
        ranked = ranked[:top]
    return dict(ranked)


def sort_orders_in_place(orders: list[Order]) -> None:
    """Сортирует список заказов на месте по убыванию суммы.
    
    Args:
        orders: Список заказов для сортировки.
    """
    orders.sort(key=lambda order: -order.kopeks)
