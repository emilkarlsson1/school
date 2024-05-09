def main():
    vuosi = -1
    ens = -1
    last = -1
    while vuosi < 0:
        vuosi = int(input("Enter the current year:\n"))
        if vuosi < 0:
            print("Enter a positive year!")

    while ens < 0:
        ens = int(input("Enter the first year to be printed:\n"))
        if ens < 0:
            print("Enter a positive year!")
    x = True

    while x:
        last = int(input("Enter the last year to be printed:\n"))
        if last < 0:
            print("Enter a positive year!")
        if last <= ens:
            print("Enter a later year than the first!")
        else:
            x = False


    print("Leap years from {:4d} to {:4d}:".format(ens, last))

    year = ens
    while year <= last:
        if (year % 4) == 0:
            if (year % 100) == 0:
                if (year % 400) == 0:
                    if year == vuosi:
                        print("{:4d} is a leap year".format(year))
                        year += 1
                    elif year < vuosi:
                        print("{:4d} was a leap year".format(year))
                        year += 1
                    else:
                        print("{:4d} will be a leap year".format(year))
                        year += 1
                else:
                    year += 1
            else:
                if year == vuosi:
                    print("{:4d} is a leap year".format(year))
                    year += 1
                elif year < vuosi:
                    print("{:4d} was a leap year".format(year))
                    year += 1
                elif year > vuosi:
                    print("{:4d} will be a leap year".format(year))
                    year += 1
                else:
                    year += 1
        else:
            year += 1

main()