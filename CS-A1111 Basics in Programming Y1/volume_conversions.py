def convert_tablespoons(tablespoons):
    return tablespoons * 14.79


def convert_fluid_ounces(fl_oz):
    return fl_oz * 29.57


def convert_cups(cups):
    return cups * 236.59


def convert_pints(pints):
    return pints * 473.18


def print_volume(millilitres):

    if millilitres >= 1000:
        e = millilitres / 1000
        print("The equivalent volume in metric units is {0:.1f} l.".format(e))
    elif millilitres >= 100:
        e = millilitres / 100
        print("The equivalent volume in metric units is {0:.1f} dl.".format(e))
    else:
        print("The equivalent volume in metric units is {0:.1f} ml.".format(millilitres))


def main():

    p = True
    x = 0
    print("The program converts US volume units into metric volume units.")
    while p:
        x = int(input("Choose the starting unit.\n1 - Tablespoon\n2 - Fluid ounce\n3 - Cup\n4 - Pint\n"))
        if x > 0:
            if x < 5:
                p = False
            else:
                p = True

    y = 0
    z = 0

    if x == 1:
        y = float(input("What is the volume in tablespoons?\n"))
        z = convert_tablespoons(y)
        print_volume(z)
    elif x == 2:
        y = float(input("What is the volume in fluid ounces?\n"))
        z = convert_fluid_ounces(y)
        print_volume(z)
    elif x == 3:
        y = float(input("What is the volume in cups?\n"))
        z = convert_cups(y)
        print_volume(z)
    elif x == 4:
        y = float(input("What is the volume in pints?\n"))
        z = convert_pints(y)
        print_volume(z)


main()