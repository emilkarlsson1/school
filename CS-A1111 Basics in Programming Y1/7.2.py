def main():

    sanat = []
    try:
        file = open("words.txt", 'r')
        for line in file:
            line = line.rstrip()
            sanat.append(line)
        file.close()

        print("Enter the text to be spell-checked (empty line to end input).")

        riv = input()
        syot = []
        while riv != '':
            riv = riv.split()
            syot.append(riv)
            riv = input()

        i = 0
        count = 0
        print("Checked text, typos highlighted with '*'")
        for sana in syot:
            print(">>", end='')
            for i in range(len(sana)):
                if sana[i].lower() in sanat:
                    print("", sana[i], end='')
                else:
                    print(" *{:s}*".format(sana[i]), end='')
                    count += 1
            print("")
        if count == 0:
            print("The text was clean.")
        else:
            print("There were", count, "typos.")
    except OSError:
        print("Error in reading the file '{:s}'. Program ends.".format(file))


main()
