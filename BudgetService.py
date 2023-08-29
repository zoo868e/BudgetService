import string
import datetime
import calendar
class Budget(object):
    def __init__(self, YearMonth: string, Amount: int):
        self.YearMonth = YearMonth
        self.Amount = Amount
class BudgetService(object):
    def __init__(self):
        pass

    def query(self, start: datetime, end: datetime) -> float:
        self.Budgets = getAll()
        Budgets_list = {}
        ret: float = 0
        for Budget in self.Budgets:
            Budgets_list[Budget.YearMonth] = Budget.Amount
        difference_date = end - start
        if start < end:
            return 0
        while start != end:
            month = start.strftime('%Y%m')
            today_budget = Budgets_list[month] / calendar.monthrange(start.year, start.month)
            ret += today_budget
            start += datetime.timedelta(days=1)
        return ret


def getAll() -> [Budget]:
    return [Budget("202308", 123)]