class Koira:

    ALOITTELIJA = 1
    HARJOITTELIJA = 2
    KESKITAITOINEN = 3
    TAITAJA = 4
    TOSITAITURI = 5

    TEMPPUTASOT = ["-", "aloittelija", "harjoittelija", "keskitaitoinen", "taitaja", "tositaituri"]

    TOSI_VASYNYT = 1
    VASYNYT = 2
    NEUTRAALI = 3
    VIRKEA = 4
    TOSI_VIRKEA = 5

    ENERGIATASOT = ["-", "tosi vasynyt", "vasynyt", "neutraali", "virkea", "tosi virkea"]

    TOSI_NALKAINEN = 1
    NALKAINEN = 2
    NEUTRAALI = 3
    KYLLAINEN = 4
    TOSI_KYLLAINEN = 5

    NALKATASOT = ["-", "tosi nalkainen", "nalkainen", "neutraali", "kyllainen", "tosi kyllainen"]

    def __init__(self, name):
        # Määrittää uuden koiran
        self.__nimi = name
        self.__tempputaso = 1
        self.__energia = 4
        self.__nalka = 4

    def kerro_nimi(self):
        return self.__nimi

    def kerro_tempputaso(self):
        return self.__tempputaso

    def kerro_energia(self):
        return self.__energia

    def kerro_nalka(self):
        return self.__nalka

    def juokse(self, maara):
        eka = self.__energia - maara
        if eka >= 1:
            self.__energia -= maara
            return maara
        else:
            if self.__energia == 1:
                self.__energia = 1
                return 0
            else:
                alku = self.__energia
                self.__energia = 1
                return alku - self.__energia

    def leiki(self, maara):
        eka = self.__nalka - maara
        if eka >= 1:
            self.__nalka -= maara
            return maara
        else:
            if self.__nalka == 1:
                self.__nalka = 1
                return 0
            else:
                alku = self.__nalka
                self.__nalka = 1
                return alku - self.__nalka

    def nuku(self, maara):
        eka = self.__energia
        loppu = self.__energia + maara
        if loppu > 5:
            self.__energia = 5
            return self.__energia - eka
        else:
            self.__energia += maara
            return maara

    def syo(self, maara):
        eka = self.__nalka
        loppu = self.__nalka + maara
        if loppu > 5:
            self.__nalka = 5
            return self.__nalka - eka
        else:
            self.__nalka += maara
            return maara

    def tee_temppu(self, vaikeusaste):
        if self.__tempputaso >= vaikeusaste:
            if self.__tempputaso < 5:
                if self.__tempputaso == vaikeusaste:
                    self.__tempputaso += 1
            return True
        else:
            return False

    def __str__(self):
        return "{}, taitotaso: {}\nEnergia: {}\nKyllaisyys: {}".format(self.kerro_nimi(),
                                                                       self.TEMPPUTASOT[self.__tempputaso],
                                                                       self.ENERGIATASOT[self.__energia],
                                                                       self.NALKATASOT[self.__nalka])
