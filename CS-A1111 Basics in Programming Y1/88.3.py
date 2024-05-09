def main():
    singletaps = 0
    jumps = 0
    holds = 0
    mines = 0
    measures = 1
    tiedot = []
    p = 0
    hold_on = True
    try:
        filename = input("Enter the file with the rhythm pattern:\n")
        file = open(filename, 'r')

        for rivi in file:
            rivi = rivi.rstrip()
            tiedot.append(rivi)
        file.close()

    except OSError:
        print("Could not open the file {:s}, try again.".format(filename))
    f = True
    y = ''
    for i in range(0, len(tiedot)):
        y = tiedot[i].split(" ")

        if y[0][0] == ',':
            measures += 1
        else:
            eka = y[0][0]
            toka = y[0][1]
            kol = y[0][2]
            nel = y[0][3]
            o = 0
            while o < 4:
                if y[0][o] == 'M':
                    mines += 1
                o += 1
            if eka == '2':
                x = 1
                while x < 4:
                    if y[0][x] == '2':
                        jumps += 1
                        break
                    else:
                        x += 1
            elif toka == '2':
                x = 0
                while x < 4:
                    if x == 1:
                        x += 1
                    elif y[0][x] == '2':
                        jumps += 1
                        break
                    else:
                        x += 1
            elif kol == '2':
                x = 0
                while x < 4:
                    if x == 2:
                        x += 1
                    elif y[0][x] == '2':
                        jumps += 1
                        break
                    else:
                        x += 1
            elif nel == '2':
                x = 0
                while x < 3:
                    if y[0][x] == '2':
                        jumps += 1
                        break
                    else:
                        x += 1
            if eka == '1':
                x = 1
                u = True
                while x <= 3:
                    if x == 0:
                        x += 1
                    elif y[0][x] == '1':
                        jumps += 1
                        u = False
                        break
                    elif y[0][x] == '2':
                        jumps += 1
                        u = False
                        break
                    else:
                        x += 1
                if u:
                    singletaps += 1
            elif toka == '1':
                x = 0
                u = True
                while x <= 3:
                    if x == 1:
                        x += 1
                    elif y[0][x] == '1':
                        jumps += 1
                        u = False
                        break
                    elif y[0][x] == '2':
                        jumps += 1
                        u = False
                        break
                    else:
                        x += 1
                if u:
                    singletaps += 1
            elif kol == '1':
                x = 0
                u = True
                while x <= 3:
                    if x == 2:
                        x += 1
                    elif y[0][x] == '1':
                        jumps += 1
                        u = False
                        break
                    elif y[0][x] == '2':
                        jumps += 1
                        u = False
                        break
                    else:
                        x += 1
                if u:
                    singletaps += 1
            elif nel == '1':
                x = 0
                u = True
                while x < 3:
                    if x == 3:
                        break
                    elif y[0][x] == '1':
                        jumps += 1
                        u = False
                        break
                    elif y[0][x] == '2':
                        jumps += 1
                        u = False
                        break
                    else:
                        x += 1
                if u:
                    singletaps += 1

            if eka == '2':
                p = i +1
                t = True
                while t:
                    if p < len(tiedot):
                        u = tiedot[p].split(" ")
                        if u[0][0] == ',':
                            p += 1
                        elif u[0][0] != '0':
                            if u[0][0] == '3':
                                holds += 1
                                t = False
                            elif u[0][0] == 'M' or '1' or '2':
                                print("Line {:d}, column 1: an object conflicts"
                                      " with a hold still in place.".format(p+1))
                                print("An overview file was not created.")
                                f = False
                                t = False
                        else:
                            p += 1
                    else:
                        t = False

            if toka == '2':
                p = i +1
                t = True
                while t:
                    if p < len(tiedot):
                        u = tiedot[p].split(" ")
                        if u[0][0] == ',':
                            p += 1
                        elif u[0][1] != '0':
                            if u[0][1] == '3':
                                holds += 1
                                t = False
                            elif u[0][1] == 'M' or '1' or '2':
                                print("Line {:d}, column 2: an object conflicts"
                                      " with a hold still in place.".format(p+1))
                                print("An overview file was not created.")
                                f = False
                                t = False
                        else:
                            p += 1
                    else:
                        t = False

            if kol == '2':

                p = i +1
                t = True
                while t:
                    if p < len(tiedot):
                        u = tiedot[p].split(" ")
                        if u[0][0] == ',':
                            p += 1
                        elif u[0][2] != '0':
                            if u[0][2] == '3':
                                holds += 1
                                t = False
                            elif u[0][2] == 'M' or '1' or '2':
                                print("Line {:d}, column 3: an object conflicts"
                                      " with a hold still in place.".format(p+1))
                                print("An overview file was not created.")
                                f = False
                                t = False
                        else:
                            p += 1
                    else:
                        t = False

            if nel == '2':

                p = i + 1
                t = True
                while t:
                    if p < len(tiedot):
                        u = tiedot[p].split(" ")
                        if u[0][0] == ',':
                            p += 1
                        elif u[0][3] != '0':
                            if u[0][3] == '3':
                                holds += 1
                                t = False
                            elif u[0][3] == 'M' or '1' or '2':
                                print("Line {:d}, column 4: an object conflicts"
                                      " with a hold still in place.".format(p+1))
                                print("An overview file was not created.")
                                f = False
                                t = False

                        else:
                            p += 1
                    else:
                        t = False

            r = 0
            t = 0

            if eka == '3':
                t = i
                alku = i
                u = tiedot[t].split(" ")

                while t >= 0:

                    u = tiedot[t - 1].split(" ")
                    if u[0][0] == ',':
                        t -= 1
                    elif u[0][0] == '2':
                        break
                    elif u[0][0] == '3':
                        print("A hold tail without hold head in line {:d}, column {:d}.".format(alku + 1, 1))
                        hold_on = False
                        break
                    else:
                        t -= 1
                if t <= 0:
                    print("A hold tail without hold head in line {:d}, column {:d}.".format(alku + 1, 1))
                    hold_on = False
                    break

            if toka == '3':
                t = i
                alku = i
                u = tiedot[t].split(" ")

                while t >= 0:
                    u = tiedot[t - 1].split(" ")
                    if u[0][0] == ',':
                        t -= 1
                    elif u[0][1] == '2':
                        break
                    elif u[0][1] == '3':
                        print("A hold tail without hold head in line {:d}, column {:d}.".format(alku + 1, 2))
                        hold_on = False
                        break
                    else:
                        t -= 1
                if t == 0:
                    print("A hold tail without hold head in line {:d}, column {:d}.".format(alku + 1, 2))
                    hold_on = False
                    break

            if kol == '3':
                t = i
                alku = i
                u = tiedot[t].split(" ")

                while t >= 0:
                    u = tiedot[t - 1].split(" ")
                    if u[0][0] == ',':
                        t -= 1
                    elif u[0][2] == '2':
                        break
                    elif u[0][2] == '3':
                        print("A hold tail without hold head in line {:d}, column {:d}.".format(alku + 1, 3))
                        hold_on = False
                        break
                    else:
                        t -= 1
                if t == 0:
                    print("A hold tail without hold head in line {:d}, column {:d}.".format(alku + 1, 3))
                    hold_on = False
                    break
            if nel == '3':
                t = i
                alku = i
                u = tiedot[t].split(" ")

                while t >= 0:
                    u = tiedot[t - 1].split(" ")
                    if u[0][0] == ',':
                        t -= 1
                    elif u[0][3] == '2':
                        break
                    elif u[0][3] == '3':
                        print("A hold tail without hold head in line {:d}, column {:d}.".format(alku + 1, 4))
                        hold_on = False
                        break
                    else:
                        t -= 1
                if t == 0:
                    print("A hold tail without hold head in line {:d}, column {:d}.".format(alku + 1, 4))
                    hold_on = False
                    break
    if p == len(tiedot):
        print("Hold tail(s) missing at the end of the file.")
        print("An overview file was not created.")
    elif not hold_on:
        print("An overview file was not created.")
    elif f:
        tt = []
        q = 0
        while q < (len(filename) - 4):
            tt.append(filename[q])
            q += 1
        tt.append("_overview.txt")
        tt = "".join(tt)

        ww = []
        a = 0
        while a < (len(filename) - 4):
            ww.append(filename[a])
            a += 1
        ww.append(".txt")
        ww = "".join(ww)

        ff = open(tt, 'w')
        ff.write("{:s}\n".format(ww))
        ff.write("Single taps: {:d}\n".format(singletaps))
        ff.write("Jumps: {:d}\n".format(jumps))
        ff.write("Holds: {:d}\n".format(holds))
        ff.write("Mines: {:d}\n".format(mines))
        ff.write("Measures: {:d}".format(measures))
        print("An overview of '{:s}' was written in '{:s}'".format(filename, tt))
        ff.close()


main()
