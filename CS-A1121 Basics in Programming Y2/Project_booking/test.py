import unittest
from gui import GUI
import sys
from PyQt5.QtWidgets import QApplication


class Test(unittest.TestCase):
    def test_button(self):
        global app  # Use global to prevent crashing on exit
        app = QApplication(sys.argv)
        self.gui = GUI()
        self.assertFalse(self.gui.calendar.accept_pressed, "Should not be pressed")







if __name__ == "__main__":
    unittest.main()


