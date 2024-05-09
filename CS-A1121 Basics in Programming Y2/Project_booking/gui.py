from PyQt5 import QtWidgets, QtCore, QtGui
from calendar import Calendar
from booking import Booking

class GUI(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        QtWidgets.QMessageBox.about(self, "Ajanvarausjärjestelmä", "Tervetuloa hotellin ajanvarausjärjestelmään! \n")
        self.setCentralWidget(QtWidgets.QWidget())
        self.layout = QtWidgets.QHBoxLayout()
        self.centralWidget().setLayout(self.layout)
        self.calendar = Calendar()
        self.booking = Booking()
        self.init_window()
        self.init_question()
        self.init_buttons()
        self.layout.addWidget(self.calendar)

        self.setLayout(self.layout)

    def init_text(self):
        self.label = QtWidgets.QLabel("Painoit")
        self.layout.addWidget(self.label)

    def init_buttons(self):
        self.quit_button = QtWidgets.QPushButton("Poistu ohjelmasta")
        self.quit_button.clicked.connect(lambda:self.close())
        self.layout.addWidget(self.quit_button,0)

        self.acccept_button = QtWidgets.QPushButton("Hyväksy")
        self.acccept_button.clicked.connect(lambda: self.calendar.pick_date())
        if self.calendar.accept_pressed:
            self.acccept_button.setEnabled(False)
        self.layout.addWidget(self.acccept_button,0)

    def init_textbox(self):
        self.topLayout = QtWidgets.QFormLayout()
        self.topLayout.addRow("Some Text:", QtWidgets.QLineEdit())
        self.layout.addLayout(self.topLayout)

    def init_question(self):
        self.acccept2_button = QtWidgets.QPushButton("OK")
        self.acccept2_button.clicked.connect(lambda: self.booking.clicked())

        self.layout.addWidget(self.acccept2_button)
        info = QtWidgets.QVBoxLayout()
        form = QtWidgets.QFormLayout()

        self.booking.nimi = QtWidgets.QLineEdit()
        self.booking.sukunimi = QtWidgets.QLineEdit()
        self.booking.katuosoite = QtWidgets.QLineEdit()
        self.booking.postinumero = QtWidgets.QLineEdit()
        self.booking.postitoimipaikka = QtWidgets.QLineEdit()
        self.booking.puhelin = QtWidgets.QLineEdit()
        self.booking.sahkoposti = QtWidgets.QLineEdit()

        form.addRow("Etunimi:", self.booking.nimi)
        form.addRow("Sukunimi:", self.booking.sukunimi )
        form.addRow("Katuosoite:", self.booking.katuosoite)
        form.addRow("Postinumero:", self.booking.postinumero)
        form.addRow("Postitoimipaikka:", self.booking.postitoimipaikka)
        form.addRow("Puhelin:", self.booking.puhelin)
        form.addRow("Sähköposti:", self.booking.sahkoposti)

        info.addLayout(form)
        self.layout.addLayout(info)

    def init_window(self):

        self.setGeometry(300,300,800,800)
        self.setWindowTitle('Varausjarjestelma')
        self.show()
