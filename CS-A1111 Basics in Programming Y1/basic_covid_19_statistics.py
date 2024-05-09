def main():
    rivi = input("What is the population of the area?\n")
    ihm = int(rivi)
    rivi = input("How many COVID-19 cases have been identified so far?\n")
    todet = int(rivi)
    rivi = input("How many deaths have been attributed to COVID-19?\n")
    kuol = int(rivi)

    tapaukset = (todet / ihm) * 1000000
    kuoltapaukset = (kuol / ihm) * 1000000
    kuolemaprosentti = (kuol / todet) * 100

    print("As for now")
    print(kuolemaprosentti, "% of known cases have resulted in death.")
    print("There are")
    print(tapaukset, "cases per 100 000 population")
    print(kuoltapaukset, "deaths per 100 000 population")
main()





