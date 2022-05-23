# Entry point for the application

# Import all expense, income and year objects
# import expense_list as el
# import income_list as il
# import year_obj as yr
from datetime import date
from app_window import Application


def main():
    """
    runs the main application loop, loads
    the necessary files on startup and
    calls the functions to display the main
    page UI elements.
    """
    # testing
    print("Program Started")

    # Main application object
    app = Application()

    # Start application loop
    app.get_app().MainLoop()

    # testing
    print("Program Ended")


def get_date():

    current_date = str(date.today())

    # Returns a reformatted date in month, day, year format
    return current_date[5:7] + '/' \
        + current_date[8:] + '/' \
        + current_date[:4]


if __name__ == "__main__":
    main()
