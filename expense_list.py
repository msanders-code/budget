# Linked list and Node objects to build the expense list

# LinkedList Node object to hold expense data
class Expense:

    def __init__(self, retailer, total, details):
        # Store name
        self._retailer = retailer
        # Purchase total
        self._purchase_tot = total
        # Items bought/notes about the purchase
        self._details = details
        # Pointer to next link in the list
        self._next = None

    def get_retailer(self):
        return self._retailer

    def get_purchase_tot(self):
        return self._purchase_tot

    def get_details(self):
        return self._details

    def get_next(self):
        return self._next

    def set_retailer(self, new_retailer):
        self._retailer = new_retailer
        return

    def set_purchase_tot(self, new_tot):
        self._purchase_tot = new_tot
        return

    def set_details(self, new_details):
        self._details = new_details
        return

    def set_next(self, next_link):
        self._next = next_link
        return


# LinkedList of expenses for the month
class ExpenseList:

    def __init__(self):
        # Total monthly cost
        self._total_cost = 0.00
        # First link in the list
        self._head = None
        # Last link in the list
        self._tail = None

    def get_total_cost(self):
        return self._total_cost

    def get_head(self):
        return self._head

    def get_tail(self):
        return self._tail

    # Updates the total monthly cost
    def set_total_cost(self):
        # add the last expense to the total cost
        self._total_cost += self._tail.get_purchase_tot()
        return

    def update_total_cost(self):
        # Set expense to head of expense list
        expense = self._head
        tot = 0.00

        # Run through the expense list and up expenses for new total
        while expense is not None:
            tot += expense.get_purchase_tot()
            expense = expense.get_next()

        # Reset new total
        self._total_cost = tot
        return

    def set_head(self, node):
        self._head = node
        return

    def set_tail(self, node):
        self._tail = node
        return
