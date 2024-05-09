def summat(n, m):
    si = {"J": 1, "kJ": 1e3, "MJ": 1e6, "GJ": 1e9, "TJ": 1e12}
    y = n * si[m]

    return y


def merkki(luku):

    merkki = ''
    if luku < 1e3:
        luku = luku / 1
        merkki = "J"
    elif 1e3 <= luku < 1e6:
        luku = luku / 1e3
        merkki = "kJ"
    elif 1e6 <= luku < 1e9:
        luku = luku / 1e6
        merkki = "MJ"
    elif 1e9 <= luku < 1e12:
        luku = luku / 1e9
        merkki = "GJ"
    elif 1e12 <= luku:
        luku = luku / 1e12
        merkki = "TJ"

    return luku, merkki


def main():
    si = {"J": 1, "kJ": 1e3, "MJ": 1e6, "GJ": 1e9, "TJ": 1e12}
    summa = 0
    tiedot = []

    try:
        filename = input("Enter the name of the production file:\n")
        file = open(filename, 'r')
        line = file.readline()
        while line != "":
            line = line.rstrip()
            tiedot.append(line)
            line = file.readline()

        file.close()
        # print(tiedot)
        # print(merkki(summa(tiedot)))
    except OSError:
        print("Error in reading the file '{:s}'.".format(filename))

    rivi = 1
    err1 = 0
    err2 = 0
    err3 = 0
    for l in tiedot:
        line = l.split(";")

        if len(line) != 3:
            print("Incorrect info  in line # {:d}:, "
                  "expected 3 semicolon separated parts, found {:d}. "
                  "The line is: {}".format(rivi, len(line), l))
            err1 += 1
        else:
            try:
                nro = float(line[1])
                unit = line[2]
                if unit not in si:
                    print("Incorrect unit  in line # {:d}: '{}'".format(rivi, line[2]))
                    err2 += 1
                else:
                    s = summat(nro, unit)
                    summa += s
            except ValueError:
                print("Incorrect value in line # {:d}: '{}'".format(rivi, line[1]))
                err3 += 1
        rivi += 1

    if err1 or err2 or err3 != 0:
        print("")
    if err1 != 0:
        print("Warning: there were {:d} lines with incorrect number of fields."
              " These are count as zeros and may affect the result!".format(err1))
    if err3 != 0:
        print("Warning: there were {:d} lines with incorrect values."
              " These are count as zeros and may affect the result!".format(err3))
    if err2 != 0:
        print("Warning: there were {:d} lines with incorrect units."
              " These are count as zeros and may affect the result!".format(err2))
    if err1 or err2 or err3 != 0:
        print("")

    if rivi > 1:
        rivi -= 1
        errtot = err1 + err2 + err3
        valid = rivi - errtot
        print("The file contains {:d} lines, out of which {:d} contain valid production data.".format(rivi, valid))
        ss, mm = merkki(summa)

        if valid > 0:
            print("The total production of the data is {} {:s}.".format(ss, mm))
            kesk = summa / valid
            sskesk, mmkesk = merkki(kesk)
            print("Average daily production of valid lines is {} {:s}.".format(sskesk, mmkesk))



main()
