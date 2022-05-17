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
        self._total = total
        # Items bought/notes about the purchase
        self._details = details

    def get_date(self):
        return self._date

    def get_retailer(self):
        return self._retailer

    def get_total(self):
        return self._total

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

    def set_total(self, new_total):
        self._total = new_total
        return

    def set_details(self, new_details):
        self._details = new_details
        return

    def set_next(self, next_link):
        self._next = next_link
        return

    # Greater than or equal to comparison definition for the expense object
    def __ge__(self, expense):
        return int(self._date[3:5]) >= int(expense.get_date()[3:5])

    # Less than comparison definition for the expense object
    def __lt__(self, expense):
        return int(self._date[3:5]) < int(expense.get_date()[3:5])


# LinkedList of expenses for the month
class ExpenseList:

    def __init__(self, node):
        # Total monthly cost
        self._total = node.get_total()
        # First link in the list
        self._head = node
        # Last link in the list
        self._tail = node

    def get_total(self):
        return self._total

    def get_head(self):
        return self._head

    def get_tail(self):
        return self._tail

    # Updates total monthly cost
    def update_total(self):

        # Set expense to head of expense list
        item = self._head
        total = 0.00

        # Add up expenses for new total
        while item is not None:
            total += item.get_total()
            item = item.get_next()

        # Reset new total
        self._total = total
        return

    def set_head(self, node):
        self._head = node
        return

    def set_tail(self, node):
        self._tail = node
        return

    # Adds an item to the list while maintaining ascending order by date
    def add_item_to_list(self, node):

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
            while node > curr.get_next():
                curr = curr.get_next()

            # Insert the new node into list
            node.set_next(curr.get_next())
            curr.set_next(node)

        return
