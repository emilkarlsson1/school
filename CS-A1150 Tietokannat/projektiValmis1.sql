--
-- File generated with SQLiteStudio v3.3.1 on Wed May 12 19:47:55 2021
--
-- Text encoding used: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: Asiakas
CREATE TABLE Asiakas (
    asiakasNro  TEXT PRIMARY KEY NOT NULL,
    nimi        TEXT,
    postinumero TEXT NOT NULL
);
INSERT INTO Asiakas (asiakasNro, nimi, postinumero) VALUES ('A-1', 'Niilo Hienonen', '02140');
INSERT INTO Asiakas (asiakasNro, nimi, postinumero) VALUES ('A-2', 'Sauli Niinist?', '02150');
INSERT INTO Asiakas (asiakasNro, nimi, postinumero) VALUES ('A-3
', 'Rami Ghoniem', '02150');
INSERT INTO Asiakas (asiakasNro, nimi, postinumero) VALUES ('A-4', 'Niilo Heinonen', '02140');
INSERT INTO Asiakas (asiakasNro, nimi, postinumero) VALUES ('A-5', 'Pekka Poute', '02600');

-- Table: Erikoisruokavalio
CREATE TABLE Erikoisruokavalio (
    nimi TEXT PRIMARY KEY );

-- Table: Hinta
CREATE TABLE Hinta (
    tuoteID        TEXT REFERENCES RuokaTuote (tuoteID) NOT NULL,
    maara          REAL NOT NULL,
    poikkeama      REAL,
    voimassaolo    TEXT,
    hinta_historia REAL,
    PRIMARY KEY (
        tuoteID
    )
    
    CHECK (maara >= 0)
);
INSERT INTO Hinta (tuoteID, maara, poikkeama, voimassaolo, hinta_historia) VALUES ('001', 0.29, NULL, NULL, NULL);
INSERT INTO Hinta (tuoteID, maara, poikkeama, voimassaolo, hinta_historia) VALUES ('009', 2.29, NULL, NULL, 1.79);
INSERT INTO Hinta (tuoteID, maara, poikkeama, voimassaolo, hinta_historia) VALUES ('010', 0.19, NULL, NULL, NULL);
INSERT INTO Hinta (tuoteID, maara, poikkeama, voimassaolo, hinta_historia) VALUES ('008', 0.55, NULL, NULL, 0.59);
INSERT INTO Hinta (tuoteID, maara, poikkeama, voimassaolo, hinta_historia) VALUES ('007', 0.45, NULL, NULL, NULL);
INSERT INTO Hinta (tuoteID, maara, poikkeama, voimassaolo, hinta_historia) VALUES ('006', 3.89, NULL, NULL, 4.2);
INSERT INTO Hinta (tuoteID, maara, poikkeama, voimassaolo, hinta_historia) VALUES ('005', 3.59, NULL, NULL, NULL);
INSERT INTO Hinta (tuoteID, maara, poikkeama, voimassaolo, hinta_historia) VALUES ('004', 2.4, NULL, NULL, 2.2);
INSERT INTO Hinta (tuoteID, maara, poikkeama, voimassaolo, hinta_historia) VALUES ('003', 1.15, 1.2, '2001', 1.1);
INSERT INTO Hinta (tuoteID, maara, poikkeama, voimassaolo, hinta_historia) VALUES ('002', 0.55, NULL, NULL, 0.6);

-- Table: Kauppaketju
CREATE TABLE Kauppaketju (
    kauppaketjuNimi TEXT PRIMARY KEY NOT NULL
);
INSERT INTO Kauppaketju (kauppaketjuNimi) VALUES ('Alepa');

-- Table: Keraajat
CREATE TABLE Keraajat (
    tuovuoro  TEXT,
    maara     INT,
    myymalaID  TEXT REFERENCES Myymala (myymalaID),
    keraajaID TEXT,
    kiire     INT,
    PRIMARY KEY (
        keraajaID,
        tuovuoro
    )
);
INSERT INTO Keraajat (tuovuoro, maara, myymalaID, keraajaID, kiire) VALUES ('aamu', 10, 'M-05', 'Ke-04', 1);
INSERT INTO Keraajat (tuovuoro, maara, myymalaID, keraajaID, kiire) VALUES ('aamu', 5, 'M-01', 'Ke-03', 1);
INSERT INTO Keraajat (tuovuoro, maara, myymalaID, keraajaID, kiire) VALUES ('aamu', 3, 'M-02', 'Ke-02', 0);
INSERT INTO Keraajat (tuovuoro, maara, myymalaID, keraajaID, kiire) VALUES ('aamu', 5, 'M-01', 'Ke-01', 1);

-- Table: Korvaavuus
CREATE TABLE Korvaavuus (korvattavaID TEXT, korvaaID TEXT, kuvaus TEXT, PRIMARY KEY (korvattavaID, korvaaID));
INSERT INTO Korvaavuus (korvattavaID, korvaaID, kuvaus) VALUES ('001', '002', 'pasta');
INSERT INTO Korvaavuus (korvattavaID, korvaaID, kuvaus) VALUES ('005', '006', 'pasta');
INSERT INTO Korvaavuus (korvattavaID, korvaaID, kuvaus) VALUES ('003', '004', 'olut');
INSERT INTO Korvaavuus (korvattavaID, korvaaID, kuvaus) VALUES ('003', '033', 'olut');

-- Table: Kuljettajat
CREATE TABLE Kuljettajat (
    kuljettajaID    TEXT PRIMARY KEY NOT NULL,
    postinumeroalue TEXT NOT NULL
);
INSERT INTO Kuljettajat (kuljettajaID, postinumeroalue) VALUES ('K4', '02180');
INSERT INTO Kuljettajat (kuljettajaID, postinumeroalue) VALUES ('K3', '02600');
INSERT INTO Kuljettajat (kuljettajaID, postinumeroalue) VALUES ('K2', '02140');
INSERT INTO Kuljettajat (kuljettajaID, postinumeroalue) VALUES ('K1', '02150');

-- Table: Myymala
CREATE TABLE Myymala (
    myymalaID    TEXT NOT NULL,
    myymala_nimi TEXT NOT NULL,
    postinumero TEXT NOT NULL,
    PRIMARY KEY (
        myymalaID
    )
);
INSERT INTO Myymala (myymalaID, myymala_nimi, postinumero) VALUES ('M-05', 'Lepp?vaara', '02600');
INSERT INTO Myymala (myymalaID, myymala_nimi, postinumero) VALUES ('M-02', 'Keilaniemi', '02150');
INSERT INTO Myymala (myymalaID, myymala_nimi, postinumero) VALUES ('M-04', 'Laajalahti', '02140');
INSERT INTO Myymala (myymalaID, myymala_nimi, postinumero) VALUES ('M-03', 'Mankkaa', '02180');
INSERT INTO Myymala (myymalaID, myymala_nimi, postinumero) VALUES ('M-01', 'Otaniemi', '02150');

-- Table: MyymalanValikoima
CREATE TABLE MyymalanValikoima (
    myymalaID TEXT REFERENCES Myymala (myymalaID) NOT NULL,
    tuoteID   TEXT NOT NULL,
    lukumaara INT,
    paino     INT,
    PRIMARY KEY (
        myymalaID,
        tuoteID
    ),
    
    CHECK (lukumaara >= 0 AND paino >= 0)
);
INSERT INTO MyymalanValikoima (myymalaID, tuoteID, lukumaara, paino) VALUES ('M-01', '004', 150, NULL);
INSERT INTO MyymalanValikoima (myymalaID, tuoteID, lukumaara, paino) VALUES ('M-01', '008', 10, NULL);
INSERT INTO MyymalanValikoima (myymalaID, tuoteID, lukumaara, paino) VALUES ('M-01', '010', 10, NULL);
INSERT INTO MyymalanValikoima (myymalaID, tuoteID, lukumaara, paino) VALUES ('M-01', '009', 20, NULL);
INSERT INTO MyymalanValikoima (myymalaID, tuoteID, lukumaara, paino) VALUES ('M-01', '007', 10, NULL);
INSERT INTO MyymalanValikoima (myymalaID, tuoteID, lukumaara, paino) VALUES ('M-01', '006', 20, NULL);
INSERT INTO MyymalanValikoima (myymalaID, tuoteID, lukumaara, paino) VALUES ('M-01', '005', 10, NULL);
INSERT INTO MyymalanValikoima (myymalaID, tuoteID, lukumaara, paino) VALUES ('M-01', '003', 200, NULL);
INSERT INTO MyymalanValikoima (myymalaID, tuoteID, lukumaara, paino) VALUES ('M-01', '002', 30, NULL);
INSERT INTO MyymalanValikoima (myymalaID, tuoteID, lukumaara, paino) VALUES ('M-01', '001', 30, NULL);
INSERT INTO MyymalanValikoima (myymalaID, tuoteID, lukumaara, paino) VALUES ('M-02', '010', 10, NULL);
INSERT INTO MyymalanValikoima (myymalaID, tuoteID, lukumaara, paino) VALUES ('M-02', '009', 20, NULL);
INSERT INTO MyymalanValikoima (myymalaID, tuoteID, lukumaara, paino) VALUES ('M-02', '008', 10, NULL);
INSERT INTO MyymalanValikoima (myymalaID, tuoteID, lukumaara, paino) VALUES ('M-02', '007', 10, NULL);
INSERT INTO MyymalanValikoima (myymalaID, tuoteID, lukumaara, paino) VALUES ('M-02', '006', 20, NULL);
INSERT INTO MyymalanValikoima (myymalaID, tuoteID, lukumaara, paino) VALUES ('M-02', '005', 10, NULL);
INSERT INTO MyymalanValikoima (myymalaID, tuoteID, lukumaara, paino) VALUES ('M-02', '004', 150, NULL);
INSERT INTO MyymalanValikoima (myymalaID, tuoteID, lukumaara, paino) VALUES ('M-02', '003', 200, NULL);
INSERT INTO MyymalanValikoima (myymalaID, tuoteID, lukumaara, paino) VALUES ('M-02', '002', 30, NULL);
INSERT INTO MyymalanValikoima (myymalaID, tuoteID, lukumaara, paino) VALUES ('M-02', '001', 30, NULL);
INSERT INTO MyymalanValikoima (myymalaID, tuoteID, lukumaara, paino) VALUES ('M-03', '010', 10, NULL);
INSERT INTO MyymalanValikoima (myymalaID, tuoteID, lukumaara, paino) VALUES ('M-03', '009', 20, NULL);
INSERT INTO MyymalanValikoima (myymalaID, tuoteID, lukumaara, paino) VALUES ('M-03', '008', 10, NULL);
INSERT INTO MyymalanValikoima (myymalaID, tuoteID, lukumaara, paino) VALUES ('M-03', '007', 10, NULL);
INSERT INTO MyymalanValikoima (myymalaID, tuoteID, lukumaara, paino) VALUES ('M-03', '006', 20, NULL);
INSERT INTO MyymalanValikoima (myymalaID, tuoteID, lukumaara, paino) VALUES ('M-03', '005', 10, NULL);
INSERT INTO MyymalanValikoima (myymalaID, tuoteID, lukumaara, paino) VALUES ('M-03', '004', 150, NULL);
INSERT INTO MyymalanValikoima (myymalaID, tuoteID, lukumaara, paino) VALUES ('M-03', '003', 200, NULL);
INSERT INTO MyymalanValikoima (myymalaID, tuoteID, lukumaara, paino) VALUES ('M-03', '002', 30, NULL);
INSERT INTO MyymalanValikoima (myymalaID, tuoteID, lukumaara, paino) VALUES ('M-03', '001', 30, NULL);
INSERT INTO MyymalanValikoima (myymalaID, tuoteID, lukumaara, paino) VALUES ('M-03', '033', 200, NULL);

-- Table: RaakaAine
CREATE TABLE RaakaAine (tuoteID TEXT REFERENCES Ruokatuote (tuoteID) NOT NULL, nimi TEXT NOT NULL, allergeenit TEXT, maara INT, PRIMARY KEY (nimi, tuoteID), CHECK (maara >= 0));
INSERT INTO RaakaAine (tuoteID, nimi, allergeenit, maara) VALUES ('001', 'vehn?', 'gluteeni', 0.48);
INSERT INTO RaakaAine (tuoteID, nimi, allergeenit, maara) VALUES ('010', 'suola', NULL, 0.15);
INSERT INTO RaakaAine (tuoteID, nimi, allergeenit, maara) VALUES ('009', 'mozzarella', 'maito', 0.1);
INSERT INTO RaakaAine (tuoteID, nimi, allergeenit, maara) VALUES ('009', 'tomaatti', 'tuoreruoka', 0.1);
INSERT INTO RaakaAine (tuoteID, nimi, allergeenit, maara) VALUES ('009', 'vehn?', 'gluteeni', 0.1);
INSERT INTO RaakaAine (tuoteID, nimi, allergeenit, maara) VALUES ('008', 'suola', NULL, 0.2);
INSERT INTO RaakaAine (tuoteID, nimi, allergeenit, maara) VALUES ('007', 'maito', 'maito', 0.33);
INSERT INTO RaakaAine (tuoteID, nimi, allergeenit, maara) VALUES ('006', 'vesi', NULL, 0.35);
INSERT INTO RaakaAine (tuoteID, nimi, allergeenit, maara) VALUES ('006', 'kaura', 'gluteeni', 0.35);
INSERT INTO RaakaAine (tuoteID, nimi, allergeenit, maara) VALUES ('005', 'nauta', 'liha', 0.4);
INSERT INTO RaakaAine (tuoteID, nimi, allergeenit, maara) VALUES ('004', 'humala', 'alkoholi', 0.05);
INSERT INTO RaakaAine (tuoteID, nimi, allergeenit, maara) VALUES ('004', 'vesi', NULL, 0.4);
INSERT INTO RaakaAine (tuoteID, nimi, allergeenit, maara) VALUES ('004', 'vehn?', 'gluteeni', 0.15);
INSERT INTO RaakaAine (tuoteID, nimi, allergeenit, maara) VALUES ('003', 'humala', 'alkoholi', 0.02);
INSERT INTO RaakaAine (tuoteID, nimi, allergeenit, maara) VALUES ('003', 'vesi', NULL, 0.21);
INSERT INTO RaakaAine (tuoteID, nimi, allergeenit, maara) VALUES ('003', 'vehn?', 'gluteeni', 0.1);
INSERT INTO RaakaAine (tuoteID, nimi, allergeenit, maara) VALUES ('002', 'vehn?', 'gluteeni', 0.96);

-- Table: Resepti
CREATE TABLE Resepti (nimi TEXT PRIMARY KEY NOT NULL, resepti_ohje TEXT NOT NULL, erikoisruokavalio TEXT);
INSERT INTO Resepti (nimi, resepti_ohje, erikoisruokavalio) VALUES ('lihamakaronilaatikko', 'ohje:', 'G, M, L');
INSERT INTO Resepti (nimi, resepti_ohje, erikoisruokavalio) VALUES ('nyht?kauramakaronilaatikko', 'ohje:', 'G, M');

-- Table: ReseptiAine
CREATE TABLE ReseptiAine (
    tuoteID           TEXT REFERENCES RuokaTuote (tuoteID) NOT NULL,
    maara             INT,
    koko              INT,
    erikoisruokavalio TEXT,
    PRIMARY KEY (
        tuoteID
    )
    
    CHECK (maara >= 0 AND koko >= 0)
);
INSERT INTO ReseptiAine (tuoteID, maara, koko, erikoisruokavalio) VALUES ('010', 1, 0.03, NULL);
INSERT INTO ReseptiAine (tuoteID, maara, koko, erikoisruokavalio) VALUES ('008', 1, 0.2, NULL);
INSERT INTO ReseptiAine (tuoteID, maara, koko, erikoisruokavalio) VALUES ('007', 1, 0.33, 'maito');
INSERT INTO ReseptiAine (tuoteID, maara, koko, erikoisruokavalio) VALUES ('006', 1, 0.4, 'gluteeni');
INSERT INTO ReseptiAine (tuoteID, maara, koko, erikoisruokavalio) VALUES ('005', 1, 0.4, 'liha');
INSERT INTO ReseptiAine (tuoteID, maara, koko, erikoisruokavalio) VALUES ('001', 1, 0.5, 'gluteeni');

-- Table: ReseptiAineKuuluu
CREATE TABLE ReseptiAineKuuluu (tuoteID TEXT REFERENCES Reseptiaine (tuoteID) NOT NULL, resepti_nimi TEXT REFERENCES Resepti (nimi) NOT NULL, PRIMARY KEY (tuoteID, resepti_nimi));
INSERT INTO ReseptiAineKuuluu (tuoteID, resepti_nimi) VALUES ('010', 'nyht?kauramakaronilaatikko');
INSERT INTO ReseptiAineKuuluu (tuoteID, resepti_nimi) VALUES ('010', 'lihamakaronilaatikko');
INSERT INTO ReseptiAineKuuluu (tuoteID, resepti_nimi) VALUES ('008', 'nyht?kauramakaronilaatikko');
INSERT INTO ReseptiAineKuuluu (tuoteID, resepti_nimi) VALUES ('008', 'lihamakaronilaatikko');
INSERT INTO ReseptiAineKuuluu (tuoteID, resepti_nimi) VALUES ('007', 'nyht?kauramakaronilaatikko');
INSERT INTO ReseptiAineKuuluu (tuoteID, resepti_nimi) VALUES ('007', 'lihamakaronilaatikko');
INSERT INTO ReseptiAineKuuluu (tuoteID, resepti_nimi) VALUES ('006', 'nyht?kauramakaronilaatikko');
INSERT INTO ReseptiAineKuuluu (tuoteID, resepti_nimi) VALUES ('005', 'lihamakaronilaatikko');
INSERT INTO ReseptiAineKuuluu (tuoteID, resepti_nimi) VALUES ('001', 'nyht?kauramakaronilaatikko');
INSERT INTO ReseptiAineKuuluu (tuoteID, resepti_nimi) VALUES ('001', 'lihamakaronilaatikko');

-- Table: Ruokatuote
CREATE TABLE Ruokatuote (
    tuoteID           TEXT NOT NULL,
    nimi              TEXT NOT NULL,
    kuvaus TEXT NOT NULL,
    koko              INT  NOT NULL,
    rasva             INT,
    energia           INT,
    hiilihydraatit    INT,
    proteiinit        INT,
    sailytys          TEXT NOT NULL,
    erikoisruokavalio TEXT,
    PRIMARY KEY (
        tuoteID
    ),
    CHECK (koko >= 0 AND 
           rasva >= 0 AND 
           energia >= 0 AND 
           hiilihydraatit >= 0 AND 
           proteiinit >= 0) 
);
INSERT INTO Ruokatuote (tuoteID, nimi, kuvaus, koko, rasva, energia, hiilihydraatit, proteiinit, sailytys, erikoisruokavalio) VALUES ('001', 'makarooni', 'pasta', 0.5, 0, 0, 0, 0, 'huoneenl?mp?', 'gluteeni');
INSERT INTO Ruokatuote (tuoteID, nimi, kuvaus, koko, rasva, energia, hiilihydraatit, proteiinit, sailytys, erikoisruokavalio) VALUES ('010', 'suola', 'mausteet', 0.15, 0, 0, 0, 0, 'huoneenl?mp?', NULL);
INSERT INTO Ruokatuote (tuoteID, nimi, kuvaus, koko, rasva, energia, hiilihydraatit, proteiinit, sailytys, erikoisruokavalio) VALUES ('009', 'pakastepitsa', 'valmisruoka', 0.3, 0, 0, 0, 0, 'pakastin', 'gluteeni');
INSERT INTO Ruokatuote (tuoteID, nimi, kuvaus, koko, rasva, energia, hiilihydraatit, proteiinit, sailytys, erikoisruokavalio) VALUES ('008', 'liemikuutio', 'mausteet', 0.2, 0, 0, 0, 0, 'huoneenl?mp?', NULL);
INSERT INTO Ruokatuote (tuoteID, nimi, kuvaus, koko, rasva, energia, hiilihydraatit, proteiinit, sailytys, erikoisruokavalio) VALUES ('007', 'ruokakerma', 'maitotuotteet', 0.33, 0, 0, 0, 0, 'j?kaappil?mp?', 'maito');
INSERT INTO Ruokatuote (tuoteID, nimi, kuvaus, koko, rasva, energia, hiilihydraatit, proteiinit, sailytys, erikoisruokavalio) VALUES ('006', 'nyht?kaura', 'lisuke', 0.4, 0, 0, 0, 0, 'j?kaappil?mp?', 'gluteeni');
INSERT INTO Ruokatuote (tuoteID, nimi, kuvaus, koko, rasva, energia, hiilihydraatit, proteiinit, sailytys, erikoisruokavalio) VALUES ('005', 'jauheliha', 'lisuke', 0.4, 0, 0, 0, 0, 'j?kaappil?mp?', 'liha');
INSERT INTO Ruokatuote (tuoteID, nimi, kuvaus, koko, rasva, energia, hiilihydraatit, proteiinit, sailytys, erikoisruokavalio) VALUES ('004', 'vaalea lager', 'olut', 0.5, 0, 0, 0, 0, 'j?kaappil?mp?', 'gluteeni');
INSERT INTO Ruokatuote (tuoteID, nimi, kuvaus, koko, rasva, energia, hiilihydraatit, proteiinit, sailytys, erikoisruokavalio) VALUES ('003', 'koff', 'olut', 0.33, 0, 0, 0, 0, 'j?kaappil?mp?', 'gluteeni');
INSERT INTO Ruokatuote (tuoteID, nimi, kuvaus, koko, rasva, energia, hiilihydraatit, proteiinit, sailytys, erikoisruokavalio) VALUES ('002', 'spagetti', 'pasta', 1, 0, 0, 0, 0, 'huoneenl?mp?', 'gluteeni');
INSERT INTO Ruokatuote (tuoteID, nimi, kuvaus, koko, rasva, energia, hiilihydraatit, proteiinit, sailytys, erikoisruokavalio) VALUES ('011', 'erikoiSspagetti', 'pasta', 1, 0, 0, 0, 0, 'huoneenlämpö', 'gluteeniton');
INSERT INTO Ruokatuote (tuoteID, nimi, kuvaus, koko, rasva, energia, hiilihydraatit, proteiinit, sailytys, erikoisruokavalio) VALUES ('012', 'erikoisLeipa', 'leipa', 1, 0, 0, 0, 0, 'huoneenlämpö', 'gluteeniton');
INSERT INTO Ruokatuote (tuoteID, nimi, kuvaus, koko, rasva, energia, hiilihydraatit, proteiinit, sailytys, erikoisruokavalio) VALUES ('033', 'karjala', 'olut', 0.33, 0, 0, 0, 0, 'jäkaappilämpö', 'gluteeni');

-- Table: Tilaus
CREATE TABLE Tilaus (tilausID TEXT PRIMARY KEY NOT NULL, aikatiedot TEXT NOT NULL, asiakasID TEXT NOT NULL REFERENCES Asiakas (asiakasNro), hyvaksyy_korvaus INT NOT NULL DEFAULT 1);
INSERT INTO Tilaus (tilausID, aikatiedot, asiakasID, hyvaksyy_korvaus) VALUES ('T-01', '2021-05-12 10:30', 'A-1', 1);
INSERT INTO Tilaus (tilausID, aikatiedot, asiakasID, hyvaksyy_korvaus) VALUES ('T-02', '2021-05-12 11:11', 'A-2', 1);
INSERT INTO Tilaus (tilausID, aikatiedot, asiakasID, hyvaksyy_korvaus) VALUES ('T-03', '2021-05-12 10:30', 'A-1', 0);

-- Table: TilausTuote
CREATE TABLE TilausTuote (tilausID TEXT NOT NULL, tuoteID TEXT NOT NULL, lukumaara INT, paino INT, korvaavuus INT, PRIMARY KEY (tilausID, tuoteID), CHECK (lukumaara >= 0 AND paino >= 0));
INSERT INTO TilausTuote (tilausID, tuoteID, lukumaara, paino, korvaavuus) VALUES ('T-05', '010', 2, NULL, 0);
INSERT INTO TilausTuote (tilausID, tuoteID, lukumaara, paino, korvaavuus) VALUES ('T-04', '004', 5, NULL, 0);
INSERT INTO TilausTuote (tilausID, tuoteID, lukumaara, paino, korvaavuus) VALUES ('T-04', '006', 1, NULL, 0);
INSERT INTO TilausTuote (tilausID, tuoteID, lukumaara, paino, korvaavuus) VALUES ('T-03', '004', 5, NULL, 1);
INSERT INTO TilausTuote (tilausID, tuoteID, lukumaara, paino, korvaavuus) VALUES ('T-03', '003', 24, NULL, 1);
INSERT INTO TilausTuote (tilausID, tuoteID, lukumaara, paino, korvaavuus) VALUES ('T-02', '002', 1, NULL, 1);
INSERT INTO TilausTuote (tilausID, tuoteID, lukumaara, paino, korvaavuus) VALUES ('T-01', '007', 2, NULL, 0);
INSERT INTO TilausTuote (tilausID, tuoteID, lukumaara, paino, korvaavuus) VALUES ('T-01', '005', 1, NULL, 0);
INSERT INTO TilausTuote (tilausID, tuoteID, lukumaara, paino, korvaavuus) VALUES ('T-01', '003', 12, NULL, 1);

-- Table: Toimitus
CREATE TABLE Toimitus (
    reitti TEXT NOT NULL,
    myymalaID TEXT REFERENCES Myymala(myymalaID) NOT NULL,
    aikatiedot TEXT,
    kapasiteetti INT,
    PRIMARY KEY (reitti, myymalaID)
    
CHECK (kapasiteetti >= 0)
);
INSERT INTO Toimitus (reitti, myymalaID, aikatiedot, kapasiteetti) VALUES ('reitti_otaniemi', 'M-01', '2021-05-12 12:00', 8);
INSERT INTO Toimitus (reitti, myymalaID, aikatiedot, kapasiteetti) VALUES ('reitti_leppavaara', 'M-03', '2021-05-12 12:00', 8);
INSERT INTO Toimitus (reitti, myymalaID, aikatiedot, kapasiteetti) VALUES ('reitti_keilaniemi', 'M-01', '2021-05-12 12:00', 5);
INSERT INTO Toimitus (reitti, myymalaID, aikatiedot, kapasiteetti) VALUES ('reitti_keilaniemi', 'M-02', '2021-05-12 12:00', 7);

-- Index: tuoteIDindex
CREATE INDEX tuoteIDindex ON Ruokatuote(tuoteID);

-- View: gluteeniton
CREATE VIEW gluteeniton AS
    SELECT *
    FROM Ruokatuote
    WHERE erikoisruokavalio = 'gluteeniton';

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
