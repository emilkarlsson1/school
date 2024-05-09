def main():

    print("Welcome to the fair muffin distribution calculator!")
    kpl = int(input("How many muffins are there?\n"))
    lapset = int(input("How many children eating?\n"))
    aikuiset = int(input("How many adults eating?\n"))
    print("The muffins can be distributed in the following ways:")
    a = kpl // aikuiset
    p = True
    while a >= 0:
        x = kpl - (a * aikuiset)
        b = x // lapset
        y = x % lapset
        if y == 0:
            print(a, "per adult and", b, "per child.")
            a -= 1
            p = False
        else:
            a -= 1

    if p:
        print("(None) :(.\n")

main()