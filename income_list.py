# LinkedList and Node objects to build the income list

# LinkedList Node object to hold the income data
class Income:

    def __init__(self, date, gain, notes):
        # Date of income
        self._date = date
        # Income amount
        self._gain = gain
        # Notes about income
        self._notes = notes
        # Pointer to next link in list
        self._next = None

    def get_date(self):
        return self._date

    def get_gain(self):
        return self._gain

    def get_notes(self):
        return self._notes

    def get_next(self):
        return self._next

    def set_date(self, new_date):
        self._date = new_date
        return

    def set_gain(self, new_gain):
        self._gain = new_gain
        return

    def set_notes(self, new_note):
        self._notes = new_note
        return

    def set_next(self, node):
        self._next = node
        return

    # Greater than or equal to comparison definition for the income object
    def __ge__(self, gain):
        return gain.get_date() >= self._date


# Linked list of income nodes
class IncomeList:

    def __init__(self):
        # Total monthly income
        self._total_income = 0.00
        # First link in list
        self._head = None
        # Last link in list
        self._tail = None

    def get_total_income(self):
        return self._total_income

    def get_head(self):
        return self._head

    def get_tail(self):
        return self._tail

    # Updates total income after changing an income amount of a node in the list
    def update_income(self):
        # Points to the current income node in the list
        income = self._head
        tot = 0.00

        # Adds income from each node in the list to a total
        while income is not None:
            tot += income.get_gain()
            income = income.get_next()

        # Update the monthly total
        self._total_income = tot
        return

    def set_head(self, node):
        self._head = node
        return

    def set_tail(self, node):
        self._tail = node
        return

    def add_income_to_list(self, node):
        # Set the tail node's next to the new node
        self._tail.set_next(node)
        # Set the tail to point to the new node
        self._tail = node
        return
