from rich.console import Console

from app.services.calculator import calculate_average, calculate_max, calculate_min
from app.utils.formatter import format_report


def main():
    values = [5, 4, 5, 3, 5]
    average = calculate_average(values)
    minimum = calculate_min(values)
    maximum = calculate_max(values)
    console = Console()
    console.print(f"[bold green]{format_report(average, minimum, maximum)}[/bold green]")


if __name__ == "__main__":
    main()