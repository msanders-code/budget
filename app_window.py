# Main window for the app
import wx


class Application:

    def __init__(self):
        # Initializes the application
        self._app = wx.App()

        # Define base width and height for app window
        self._width = int(wx.GetDisplaySize()[0] * 0.75)
        self._height = int(wx.GetDisplaySize()[1] * 0.75)

        # Initializes the base app frame with default frame style
        self._window = wx.Frame(
            None,
            0,
            "Budget Tracker",
            size=(self._width, self._height)
        )

        # Maximize and show the app window on startup
        self._window.Maximize()
        self._window.Show()

    # Return the initialized app
    def get_app(self):
        return self._app

    # Return the Frame object
    def get_window(self):
        return self._window
