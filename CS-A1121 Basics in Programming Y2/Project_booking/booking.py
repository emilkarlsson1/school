

class Booking():
    def __init__(self):
        super().__init__()
        self.nimi = ''
        self.sukunimi = ''
        self.katuosoite = ''
        self.postinumero = ''
        self.postitoimipaikka = ''
        self.puhelin = ''
        self.sahkoposti = ''

    def clicked(self):

        print(self.nimi.text())
        print(self.sukunimi.text())
        print(self.katuosoite.text())
        print(self.postinumero.text())
        print(self.postitoimipaikka.text())
        print(self.puhelin.text())
        print(self.sahkoposti.text())
