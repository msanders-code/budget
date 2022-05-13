# Object to represent the year of expenses and income

class Year:

    _expenses_by_month = {
        "01": None, "02": None, "03": None,
        "04": None, "05": None, "06": None,
        "07": None, "08": None, "09": None,
        "10": None, "11": None, "12": None
    }
    _income_by_month = {
        "01": None, "02": None, "03": None,
        "04": None, "05": None, "06": None,
        "07": None, "08": None, "09": None,
        "10": None, "11": None, "12": None
    }

    def get_expenses_by_month(self, month):
        return self._expenses_by_month[month]

    def get_income_by_month(self, month):
        return self._income_by_month[month]

    def add_income_list(self, month, lst):
        self._income_by_month[month] = lst
        return

    def add_expense_list(self, month, lst):
        self._expenses_by_month[month] = lst
        return
