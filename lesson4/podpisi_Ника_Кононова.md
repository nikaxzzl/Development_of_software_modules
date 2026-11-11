# Практикум «Младший разработчик: первая неделя»

МДК.01.01 · аннотации типов и окружение проекта

- Студент: Ника Кононова
- Группа: РПО3
- Сдано: 11.11.2026, 18:24:09

## Рецензия

| Письмо | Результат | Баллы |
|---|---|---|
| Письмо 1 · рабочее место | 17 из 18 | 2 / 2 |
| Письмо 2 · подписи по заявкам | 7 из 10 | 3 / 4 |
| Письмо 3 · вызовы и подпись | 38 из 40 | 2 / 2 |
| Письмо 4 · подпись вручную | 1 из 4 | 0 / 2 |
| **Итого** | | **7 / 10 · хорошо** |

- Рабочее место: повторите порядок создания окружения и установки (глава 2.1, 2.3).
- Подписи по заявкам: не решены заявки 3, 8, 10. Повторите: какие данные нужны функции, а какие нет; словари и кортежи в аннотациях (глава 4.2, §2); -> None у функции без результата (глава 4.2, §1); порядок параметров со значением по умолчанию (глава 4.1, §3); запись X | None и объединение int | str (глава 4.2, §4–5).
- Вызовы и подпись: ошибки в подписи 5. Прочитайте разбор под каждой.
- Подпись вручную: не решены заявки 2, 3, 4.

## Письмо 1. Рабочее место

### Порядок команд — неверно

1. `deactivate`
2. `python -m pip freeze > requirements.txt`
3. `pip install rich`

### Первый коммит — верно 10 из 10

| Файл | Ваш ответ | Верно |
|---|---|---|
| `main.py` | в репозиторий | ✓ |
| `app/calculator.py` | в репозиторий | ✓ |
| `tests/test_calculator.py` | в репозиторий | ✓ |
| `requirements.txt` | в репозиторий | ✓ |
| `README.md` | в репозиторий | ✓ |
| `.gitignore` | в репозиторий | ✓ |
| `.venv/` | на компьютере | ✓ |
| `__pycache__/` | на компьютере | ✓ |
| `app/__pycache__/calculator.cpython-312.pyc` | на компьютере | ✓ |
| `.env` | на компьютере | ✓ |

### Вопросы из чата — верно 7 из 7

| Вопрос | Ваша причина | Верно |
|---|---|---|
| 1. Денис | Пакет установлен в другой Python, не в окружение проекта | ✓ |
| 2. Лиза | Окружение не активно в этом терминале | ✓ |
| 3. Ксюша | Зависимости проекта не записаны в requirements.txt | ✓ |
| 4. Глеб | Нет правил .gitignore для окружения и кэша | ✓ |
| 5. Марат | Список зависимостей снят не в окружении проекта | ✓ |
| 6. Оля | VS Code использует другой интерпретатор, не из .venv | ✓ |
| 7. Тимур | Окружение перенесено с другого компьютера | ✓ |

## Письмо 2. Подписи по заявкам

### 1. Колледж «Северный» · электронный журнал — верно

```python
def average_grade(grades: list[int]) -> float:
```

### 2. Колледж «Северный» · посещаемость — верно

```python
def count_absences(marks: list[str]) -> int:
```

### 3. Кофейня «Зерно» · касса — неверно

```python
def order_total(items: dict[str, int]) -> int:
```

### 4. Кофейня «Зерно» · постоянные гости — верно

```python
def find_guest_phone(guests: dict[str, str], name: str) -> str | None:
```

### 5. Фитнес-клуб «Пульс» · абонементы — верно

```python
def is_membership_active(end_date: date, today: date) -> bool:
```

### 6. Книжный магазин «Переплёт» · склад — верно

```python
def parse_quantity(value: int | str) -> int:
```

### 7. Курьерская служба «Квартал» · отчёт за день — верно

```python
def distance_bounds(distances: list[float]) -> tuple[float, float]:
```

### 8. Кофейня «Зерно» · печать чека — неверно

```python
def print_receipt(width: int = 32, lines: list[str]) -> None:
```

### 9. Колледж «Северный» · ведомость группы — верно

```python
def average_by_student(journal: dict[str, list[int]]) -> dict[str, float]:
```

### 10. Фитнес-клуб «Пульс» · карта клиента — неверно

```python
def format_name(first_name: str, last_name: str, middle_name: str = None) -> str:
```

## Письмо 3. Вызовы и подпись

| Подпись | Верно |
|---|---|
| `def average_grade(grades: list[int]) -> float:` | 8 из 8 |
| `def find_guest_phone(guests: dict[str, str], name: str) -> str \| None:` | 8 из 8 |
| `def format_name(last_name: str, first_name: str, middle_name: str \| None = None) -> str:` | 8 из 8 |
| `def parse_quantity(value: int \| str) -> int:` | 8 из 8 |
| `def print_receipt(lines: list[str], width: int = 32) -> None:` | 6 из 8 |

## Письмо 4. Подпись вручную

### 1. Колледж «Северный» · лучший студент — верно

```python
def best_student(averages: dict[str, float]) -> str| None:
```

### 2. Фитнес-клуб «Пульс» · бонусы — неверно

```python
def add_bonus(balance: int, is_vip: bool = False) -> int:
```

- параметры: balance, is_vip, а нужны balance, visits, is_vip

### 3. Курьерская служба «Квартал» · адреса — неверно

```python
def split_address(averages:str) -> tuple[str, str]:
```

- параметры: averages, а нужны address

### 4. Книжный магазин «Переплёт» · авторы — неверно

```python
def unique _authors(averges: list[str]) -> set[str]:
```

- ошибка записи: После имени функции нужна открывающая скобка (.
