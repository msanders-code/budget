# Entry point for the application

# Import all expense, income and year objects
import expense_list as el
import income_list as il
import year_obj as yr


def main():

    data = {"2022": yr.Year()}

    # test expense and expense list objects
    expense1 = el.Expense("03/23/2022", "JC Penny", 125.21, "Bought a hat, coat and some shoes.")

    # Add a new expense list to the data dictionary
    data["2022"].add_expense_list("03", el.ExpenseList(expense1))

    # Access and update the expense list from the data dictionary
    e_lst = data["2022"].get_expenses_by_month("03")
    curr_expense = e_lst.get_head()

    # print the current expenses
    print("Current Expenses:\n")
    while curr_expense is not None:
        print(f"\n{curr_expense.get_date()}\n{curr_expense.get_retailer()}\n")
        print(f"{curr_expense.get_purchase_tot()}\n{curr_expense.get_details()}\n")
        curr_expense = curr_expense.get_next()

    expense2 = el.Expense("03/21/2022", "Burger King", 20.82, "Lunch")
    e_lst.add_expense_to_list(expense2)
    e_lst.update_total_cost()

    # Print updated total cost for the month by accessing the data dictionary entry
    print(data["2022"].get_expenses_by_month("03").get_total_cost())

    # Test income and income list objects
    income1 = il.Income("01/15/2022", 1102.98, "Paycheck")

    # Add a new income list to the data dictionary
    data["2022"].add_income_list("01", il.IncomeList(income1))

    # Access and update the income list from the data dictionary
    i_lst = data["2022"].get_income_by_month("01")
    curr_gain = i_lst.get_head()

    # print the current gains
    print("Current Gains:\n")
    while curr_gain is not None:
        print(f"\n{curr_gain.get_date()}\n{curr_gain.get_gain()}\n")
        print(f"{curr_expense.get_notes()}\n")
        curr_gain = curr_gain.get_next()

    income2 = il.Income("01/31/2022", 1102.98, "Paycheck")
    i_lst.add_income_to_list(income2)
    i_lst.update_income()

    # Print updated total income for the month by accessing the data dictionary entry
    print(data["2022"].get_income_by_month("01").get_total_income())
