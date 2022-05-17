# LinkedList and Node objects to build the income list

import expense_list as el


# LinkedList Node object to hold the income data
# That inherits from the expense class
class Income (el.Expense):

    def __init__(self, date, total, details):
        super().__init__(date, "", total, details)


# Linked list of income nodes that inherits from the expense list
class IncomeList (el.ExpenseList):

    def __init__(self, node):
        super().__init__(node)
