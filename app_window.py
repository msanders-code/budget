# Main window for the app
import wx
from wx import App, Frame


class Application:
    # Initializes the application
    _app = App()

    # Initializes the base app frame with default frame style
    _window = Frame(None, 0, "Budget Tracker", size=(1000, 850))
    _window.Centre()

    # Shows the frame on the screen
    _window.Show()

    # Return the initialized app
    def get_app(self):
        return self._app

    # Return the Frame object
    def get_window(self):
        return self._window
