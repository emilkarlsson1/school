def main():

    CAFFEINE_IN_COFFEE_CUP = 120  # mg, milligrams
    CAFFEINE_IN_TEA_CUP = 40  # mg
    MAX_RECOMMENDED_INTAKE = 400  # mg
    LETHAL_DOSE = 10000  # mg

    print("The program calculates an adult's caffeine intake and gives feedback of the consumption.")

    days = int(input("How many days you wish to input?\n"))

    x = 1
    ylitys = 0
    kof = 0
    kuol = 0

    if days == 0:
        print("No consumption data entered.")
    else:
        for i in range(days):
            print("Day", x)
            x += 1
            kahvi = -1
            tee = -1
            while kahvi < 0:
                kahvi = int(input("How many cups of coffee did you drink?\n"))
                if kahvi < 0:
                    print("The number must be at least 0!")
            while tee < 0:
                tee = int(input("And how many cups of tea?\n"))
                if tee < 0:
                    print("The number must be at least 0!")

            day = (kahvi * CAFFEINE_IN_COFFEE_CUP) + (tee * CAFFEINE_IN_TEA_CUP)
            kof += day
            if day > MAX_RECOMMENDED_INTAKE:
                ylitys += 1
                if day > LETHAL_DOSE:
                    print("** Lethal dose exceeded!! **")
                    kuol += 1

    if days != 0:
        median = kof / days

        print("On average, you consumed {:.0f} mg of caffeine per day.".format(median))
        print("You exceeded the maximum recommended amount of 400 mg on", ylitys, "out of", days, "days.")

        if kuol > 0:
            print("You exceeded the lethal dose on", kuol, "days.")

main()