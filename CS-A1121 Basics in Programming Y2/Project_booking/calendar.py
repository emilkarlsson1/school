from PyQt5.QtGui import QPalette, QTextCharFormat
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets
from datetime import date


class Calendar(QtWidgets.QCalendarWidget):
    def __init__(self):
        super().__init__()
        self.begin_date = date.today()
        self.end_date = None
        self.setMinimumDate(date.today())
        self.highlight_format = QTextCharFormat()
        self.highlight_format.setBackground(self.palette().brush(QPalette.Highlight))
        self.highlight_format.setForeground(self.palette().color(QPalette.HighlightedText))
        self.accept_pressed = False
        self.clicked.connect(self.date_is_clicked)

    def bold(self, format):
        if self.begin_date and self.end_date:
            d0 = self.begin_date
            d1 = self.end_date
            while d0 <= d1:
                self.setDateTextFormat(d0, format)
                d0 = d0.addDays(1)

    def date_is_clicked(self, date):
        self.bold(QTextCharFormat())
        if QtWidgets.QApplication.instance().keyboardModifiers() & Qt.ShiftModifier and self.begin_date < date:
            self.end_date = date
            self.bold(self.highlight_format)
        else:
            self.begin_date = date
            self.end_date = None

    def pick_date(self):
        self.accept_pressed = True
        if self.accept_pressed and self.begin_date and self.end_date:
            print(self.begin_date,
                  self.end_date)

    def get_pressed(self):
        return self.accept_pressed