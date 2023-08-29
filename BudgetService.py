import string
import datetime
import calendar
class Budget(object):
    def __init__(self, YearMonth: string, Amount: int):
        self.YearMonth = YearMonth
        self.Amount = Amount
class BudgetService(object):
    def __init__(self):
        self.Budgets = BudgetRepo()

    def query(self, start: datetime, end: datetime) -> float:
        Budgets_list = self.get_budget_dict()
        ret: float = 0
        while start <= end:
            month = start.strftime('%Y%m')
            if month not in Budgets_list.keys():
                start += datetime.timedelta(days=1)
                continue
            today_budget = Budgets_list[month] / calendar.monthrange(start.year, start.month)[1]
            ret += today_budget
            start += datetime.timedelta(days=1)
        return ret

    def get_budget_dict(self) -> dict:
        ret = {}
        for Budget in self.Budgets.getAll():
            ret[Budget.YearMonth] = Budget.Amount
        return ret


class BudgetRepo(object):
    def getAll(self) -> [Budget]:
        return [Budget("202308", 123)]