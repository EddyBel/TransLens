from settings import AUTOMATIC, MODE, TRANSPARENCE, TITLE_WINDOW
from capture import Capture
from time import sleep
from util import save_text, clear_terminal
import wx

# An instance of the Capture class is created.
capture = Capture()


class DesktopController(wx.Frame):
    """A class called DesktopController is defined that inherits from wx.Frame. This class is in charge of managing the functionality next to the wx library window
    """

    def __init__(self, parent, title: str) -> None:
        """A constructor method is defined that receives a parent object and a title.

        Args:
            parent (any): Receive any other value.
            title (str): window title name
        """

        # The constructor of the parent class is called with the given arguments.
        super(DesktopController, self).__init__(parent, title=title)
        # Set the transparency of the window to 300.
        self.SetTransparent(TRANSPARENCE)
        # An empty button is created in the window.
        self.button = wx.Button(self)
        # The click event of the button is linked to the click method of the class.
        self.Bind(wx.EVT_BUTTON, self.click, self.button)
        # Sets the position of the window to the upper left corner of the screen.
        self.SetPosition(wx.Point(0, 0))
        # The window is displayed.
        self.Show()

    def translate_img(self, bbox, t):
        """A method is defined that takes a bounding box (bbox) and a translator object (t) and captures the text inside the box.
        Then, it displays the captured text and its translation in the console.

        Args:
            bbox (tupla): Delimits the space of the window to capture.
            t (any): Library that has the functions of translating.
        """

        # An image of the area bounded by the box is captured and stored in the img variable.
        img = capture.capture_window(bbox=bbox)
        # The text is extracted from the captured image and stored in the lines variable.
        lines = capture.get_text_by_img(img=img)
        # The console is cleaned.
        clear_terminal()
        # The list of lines of captured text is traversed.
        for line in lines:
            # A string is created that displays the captured text with an eye emoji 👀.
            text_capture = f"👀 {line}"
            # A string is created that displays the translation of the text captured with a globe emoji 🌍.
            try:
                text_translate = t.translate(line)
            except:
                text_translate = line
            # Both strings are printed to the console, separated by a line separator.
            print(text_capture)
            print(f"🌍 {text_translate}")
            print("-------------------------------")
            # Save text in file txt
            save_text(line, "translate")
            save_text(text_translate, "translate")
            save_text("---------------------------", "translate")

    def transcript_img(self, bbox):
        """This method gets the text from an image, and displays it in the terminal.

        Args:
            bbox (tupla): Delimit the capture of the image.
        """

        # An image of the area bounded by the box is captured and stored in the img variable.
        img = capture.capture_window(bbox=bbox)
        # The text is extracted from the captured image and stored in the lines variable.
        lines = capture.get_text_by_img(img=img)
        # The console is cleaned.
        clear_terminal()
        # The list of lines of captured text is traversed.
        for line in lines:
            # A string is created that displays the captured text with an eye emoji 👀.
            text = f"👀 {line}"
            # Print the obtained text
            print(text)
            # Save text in file txt
            save_text(line, "transcript")

    def click(self, event):
        """This function is executed every time the button is clicked.

        Args:
            event (any): Click event.
        """

        # Gets the button's dimensions and position on the screen.
        size = self.button.Size
        x1, y1 = self.button.GetScreenPosition()
        x2, y2 = x1 + size[0], y1 + size[1]
        # Defines a tuple representing the selected area
        fragment = (x1, y1, x2, y2)

        # Hide the main window
        self.Hide()

        # If the mode is "translate"
        if MODE == "TRANSLATE":
            # Import the Translate class from the translate.py file
            from translate import Translate
            # Create an instance of the Translate class
            t = Translate()
            # If the translation is done automatically
            if AUTOMATIC:
                # Infinite loop that continuously captures and translates the text in the selected area
                while True:
                    self.translate_img(bbox=fragment, t=t)
                    sleep(1)
            # If the translation is not done automatically
            else:
                # Capture and translate the text only once
                self.translate_img(bbox=fragment, t=t)

        # If the mode is "transcribe"
        elif MODE == "TRANSCRIBE":
            # If the transcription is done automatically
            if AUTOMATIC:
                # Infinite loop that continuously captures the text in the selected area
                while True:
                    self.transcript_img(bbox=fragment)
                    sleep(1)
            # If the transcription is not done automatically
            else:
                # Capture the text only once
                self.transcript_img(bbox=fragment)

        # Show the main window again
        self.Show()


if __name__ == "__main__":
    # Create an instance of the wxPython application
    app = wx.App()
    # Create an instance of the DesktopController class
    mf = DesktopController(None, title=TITLE_WINDOW)
    # Starts the main event loop of the wxPython application
    app.MainLoop()
