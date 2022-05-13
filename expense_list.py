# Linked list and Node objects to build the expense list

# LinkedList Node object to hold expense data
class Expense:

    # Pointer to next link in the list
    _next = None

    def __init__(self, date, retailer, total, details):
        # Date of expense
        self._date = date
        # Store name
        self._retailer = retailer
        # Purchase total
        self._purchase_tot = total
        # Items bought/notes about the purchase
        self._details = details

    def get_date(self):
        return self._date

    def get_retailer(self):
        return self._retailer

    def get_purchase_tot(self):
        return self._purchase_tot

    def get_details(self):
        return self._details

    def get_next(self):
        return self._next

    def set_date(self, new_date):
        self._date = new_date
        return

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

    # Greater than or equal to comparison definition for the expense object
    def __ge__(self, expense):
        return expense.get_date() >= self._date

    # Less than comparison definition for the expense object
    def __lt__(self, expense):
        return expense.get_date() < self._date


# LinkedList of expenses for the month
class ExpenseList:

    def __init__(self, node):
        # Total monthly cost
        self._total_cost = node.get_purchase_tot()
        # First link in the list
        self._head = node
        # Last link in the list
        self._tail = node

    def get_total_cost(self):
        return self._total_cost

    def get_head(self):
        return self._head

    def get_tail(self):
        return self._tail

    # Updates total monthly cost
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

    # Adds an expense to the list while maintaining ascending order by date
    def add_expense_to_list(self, node):

        if node >= self._tail:
            # Set last node to point to new node
            self._tail.set_next(node)
            # Set tail to point to new node
            self._tail = node
        elif node < self._head:
            # Set new node to point to current head
            node.set_next(self._head)
            # Set head to point to new node
            self._head = node
        else:
            curr = self._head
            # Search the list for node insertion point
            while node < curr:
                curr = curr.get_next()

            # Insert the new node into list
            node.set_next(curr.get_next())
            curr.set_next(node)
        return
