def main():
    AB = -1
    BC = -1
    ABC = -1

    while AB < 0 or BC < 0 or ABC < 0:
        AB = int(input("How many AB-zone trips do you make per month?\n"))
        BC = int(input("How many BC-zone trips do you make per month?\n"))
        ABC = int(input("How many ABC-zone trips do you make per month?\n"))
        if AB < 0 or BC < 0 or ABC < 0:
            print("The given values cannot be negative!")

    kertalippu = 2.80  # €  AB tai BC
    kertalippu2 = 4.10  # € ABC

    ABkausi = 32.80  # €
    BCkausi = 32.80  # €
    ABCkausi = 53.20  # €

    lisavyoh = 2.50  # €

    kertaliput = ((AB + BC) * kertalippu) + (ABC * kertalippu2)
    if (AB + BC) > ABC:
        if AB >= BC:
            if kertaliput < (ABkausi + ((ABC + BC) * lisavyoh)):
                if kertaliput > ABCkausi:
                    print("You should buy an ABC-zone season ticket.")
                    print("The price per month will be", ABCkausi, "euros.")
                else:
                    print("You should buy single tickets for each trip.")
                    print("The price per month will be",kertaliput, "euros.")
            else:
                lippu = ABkausi + ((BC+ABC) * lisavyoh)

                if kertaliput <= lippu:
                    print("You should buy an AB-zone season ticket and C-zone extension tickets when needed.")
                    print("The price per month will be", lippu, "euros.")
                elif lippu <= ABCkausi:
                    print("You should buy an AB-zone season ticket and C-zone extension tickets when needed.")
                    print("The price per month will be", lippu, "euros.")
                else:
                    print("You should buy an ABC-zone season ticket.")
                    print("The price per month will be", ABCkausi, "euros.")

        elif BC >= AB:
            if kertaliput < (BCkausi + ((ABC + AB) * lisavyoh)):
                if kertaliput > ABCkausi:
                    print("You should buy an ABC-zone season ticket.")
                    print("The price per month will be", ABCkausi, "euros.")
                else:
                    print("You should buy single tickets for each trip.")
                    print("The price per month will be", kertaliput, "euros.")
            else:
                lippu = BCkausi + ((ABC + AB) * lisavyoh)

                if kertaliput == lippu:
                    print("You should buy a BC-zone season ticket and A-zone extension tickets when needed.")
                    print("The price per month will be", lippu, "euros.")
                elif lippu < ABCkausi:
                    print("You should buy a BC-zone season ticket and A-zone extension tickets when needed.")
                    print("The price per month will be", lippu, "euros.")
                else:
                    print("You should buy an ABC-zone season ticket.")
                    print("The price per month will be", ABCkausi, "euros.")

    elif ABC >= (AB + BC):
        if kertaliput < ABCkausi:
            print("You should buy single tickets for each trip.")
            print("The price per month will be", kertaliput, "euros.")
        else:
            print("You should buy an ABC-zone season ticket.")
            print("The price per month will be", ABCkausi, "euros.")

main()