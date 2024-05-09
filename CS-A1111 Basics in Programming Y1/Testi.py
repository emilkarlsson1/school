# Define the function "calculate" here.

def calculate(nimi, ika):
    if ika < 18:
        i = 18 - ika
        print(nimi, ", you'll be eighteen in", i, "years.")
    elif ika > 18:
        i = ika - 18
        print(nimi, ", you turned eighteen", i, "years ago.")
    elif ika == 18:
        print(nimi, ", you probably know you are exactly 18 years old?")



def main():
    my_name = input("What is your name?\n")
    my_age = int(input("What is your age in years?\n"))
    calculate(my_name, my_age)

main()