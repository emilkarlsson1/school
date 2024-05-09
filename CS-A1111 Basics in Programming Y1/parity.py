def main():
    luku = -1

    while luku <= 0:
        luku = int(input("Montako lukua annetaan?\n"))
        if luku <= 0:
            print("Anna positiivinen arvo!")

    parillinen = 0
    pariton = 0
    print("Anna luvut omilla riveillaan.")
    for i in range(luku):
        rivi = int(input())
        jako = rivi % 2
        if jako == 0:
            parillinen += 1
        else:
            pariton += 1

    print("Lukuja annettiin", luku, "kpl.")
    print("Niista", parillinen, "on parillisia ja", pariton, "parittomia.")
main()