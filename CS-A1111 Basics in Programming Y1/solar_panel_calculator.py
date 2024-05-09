def main():
    maara = int(input("How many solar panels' energy yield do you want to calculate?\n"))
    x = (maara * 175) / 1000
    y = (maara * 175) / 80
    z = (maara * 175) / 18
    print("That number of panels gives", x, "kWh of energy each day.")
    print("That is equal to watching the TV for", y, "hours")
    print("or having", z, "led bulbs on for 10 hours per day.")
main()