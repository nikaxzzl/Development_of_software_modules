import unittest

from app.services.calculator import (
    calculate_total,
    calculate_average,
    most_expensive_day,
    category_share,
)
from app.utils.data import EXPENSES


class TestCalculator(unittest.TestCase):

    def test_total(self):
        self.assertEqual(calculate_total(EXPENSES), 7900)

    def test_average(self):
        self.assertAlmostEqual(calculate_average(EXPENSES), 790.0, places=2)

    def test_most_expensive_day(self):
        self.assertEqual(most_expensive_day(EXPENSES), (2, 2700))

    def test_category_share_food(self):
        self.assertAlmostEqual(category_share(EXPENSES, "еда"), 24.87, places=2)

    def test_category_share_housing(self):
        self.assertAlmostEqual(category_share(EXPENSES, "жильё"), 68.35, places=2)

    def test_empty_raises(self):
        for fn in (calculate_average, most_expensive_day):
            with self.assertRaises(ValueError):
                fn([])

    def test_unknown_category_raises(self):
        with self.assertRaises(ValueError):
            category_share(EXPENSES, "сувениры")


if __name__ == "__main__":
    unittest.main()