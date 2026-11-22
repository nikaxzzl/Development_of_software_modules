"""Сохранение текстового отчёта в файл."""
from pathlib import Path


def save_report(path: Path, lines: list[str]) -> int:
    """Записывает строки отчёта в текстовый файл в кодировке UTF-8.

    Args:
        path: Путь к файлу, в который нужно сохранить отчёт.
        lines: Список строк отчёта для записи.

    Returns:
        Количество записанных строк.
    """    
    with open(path, "w", encoding="utf-8") as file:
        file.write("\n".join(lines))
    return len(lines)
