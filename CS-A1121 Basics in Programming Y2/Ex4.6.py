import unittest
from datetime import date
from weekdays import weekdays


class TestWeekdays(unittest.TestCase):
    """Implement tests for weekdays here."""
    def test1(self):
        self.assertEqual(weekdays(date(2022, 1, 23), date(2022, 1, 30)), 40, "Fail1")

    def test2(self):
        self.assertEqual(weekdays(date(2022, 1, 24), date(2022, 1, 25)), 16, "Fail2")


if __name__ == "__main__":
    unittest.main()
