def main():
    i = 0
    lista = []
    luku = 1
    z = 0

    print("This program analyzes your daily pushup history. Enter a negative amount when finished.")

    while luku >= 0:
        if i == 0:
            luku = int(input("How many push-ups did you do the first day?\n"))
            if luku >= 0:
                lista.append(luku)

            else:
                print("You did not enter any data.")
                z = -1
            i = 2
        else:
            luku = int(input("How many push-ups did you do the next day?\n"))
            if luku >= 0:
                lista.append(luku)

    x = 0
    day = 1

    if z == 0:
        print("Bar graph:")
        for y in lista:
            print("Day {:3d}:".format(day), y * "#")
            day += 1
            x += y

        per = x / (len(lista))
        print("\nIn total, you performed", x, "pushups, which is roughly {:.1f} per day.".format(per))

        print("The highest daily number of pushups was", max(lista), "on day {}.".format((lista.index(max(lista))) + 1))


main()