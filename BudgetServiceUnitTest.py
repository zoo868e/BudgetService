import unittest
import unittest.mock as mock
from unittest.mock import patch
import BudgetService
import datetime


class BudgetServiceTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.BudgetService = BudgetService.BudgetService()
        getAll_patch = patch('BudgetService.BudgetRepo.getAll')
        self.fake_getAll = getAll_patch.start()

    def given_budgets(self, Budgets: list[BudgetService.Budget]):
        self.fake_getAll.return_value = Budgets

    def given_start_date(self, Year: int, Month: int, Day: int):
        self.start_date = datetime.datetime(Year, Month, Day, 15, 30, 0)

    def given_end_date(self, Year: int, Month: int, Day: int):
        self.end_date = datetime.datetime(Year, Month, Day, 15, 30, 0)

    def budget_should_be(self, expect: float):
        self.assertEqual(expect, self.BudgetService.query(self.start_date, self.end_date))

    def test_one_day(self):
        self.given_start_date(2023, 7, 15)
        self.given_end_date(2023, 7, 15)
        self.given_budgets([
            BudgetService.Budget("202307", 31),
        ])
        self.budget_should_be(1)

    def test_two_days(self):
        self.given_start_date(2023, 7, 15)
        self.given_end_date(2023, 7, 16)
        self.given_budgets([
            BudgetService.Budget("202307", 31),
        ])
        self.budget_should_be(2)

    def test_a_month(self):
        self.given_start_date(2023, 7, 1)
        self.given_end_date(2023, 7, 31)
        self.given_budgets([
            BudgetService.Budget("202307", 31),
        ])
        self.budget_should_be(31)
    def test_no_data(self):
        self.given_start_date(2023, 7, 1)
        self.given_end_date(2023, 7, 31)
        self.budget_should_be(0)

    def test_leap_month(self):
        self.given_start_date(2024, 2, 1)
        self.given_end_date(2024, 2, 29)
        self.given_budgets([
            BudgetService.Budget("202402", 2900),
        ])
        self.budget_should_be(2900)
    def test_start_later_than_end(self):
        self.given_start_date(2025, 2, 1)
        self.given_end_date(2024, 2, 29)
        self.budget_should_be(0)
    def test_cross_over_months(self):
        self.given_start_date(2023, 8, 29)
        self.given_end_date(2023, 9, 4)
        self.given_budgets([
            BudgetService.Budget("202308", 3100),
            BudgetService.Budget("202309", 30)
        ])
        self.budget_should_be(304)
    def test_not_leap_month_year(self):
        self.given_start_date(2023, 2, 2)
        self.given_end_date(2023, 2, 28)
        self.given_budgets([
            BudgetService.Budget("202302", 280),
        ])
        self.budget_should_be(270)

    def test_cross_years(self):
        self.given_start_date(2023, 12, 30)
        self.given_end_date(2024, 1, 5)
        self.given_budgets([
            BudgetService.Budget("202312", 3100),
            BudgetService.Budget("202401", 31),
        ])
        self.budget_should_be(205)

if __name__ == '__main__':
    unittest.main()
