from app.services.calculator import calculate_total, calculate_average

def test_total():
    exp = [{"amount": 540}, {"amount": 260}]
    if calculate_total(exp) != 800:
        print("test_total: False")
    else:
        print("test_total: OK")


def test_average():
    exp = [{"amount": 540}, {"amount": 260}]
    if calculate_average(exp) != 400.0:
        print("test_average: False")
    else:
        print("test_average: OK")


def test_empty():
    try:
        calculate_average([])
        print("test_empty: False")
    except ValueError:
        print("test_empty: OK")


if __name__ == "__main__":
    test_total()
    test_average()
    test_empty()