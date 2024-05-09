def main():

    a = int(input("First number:\n"))
    b = int(input("Second number:\n"))

    aa = a
    bb = b
    p = True

    while p:

        q = a // b
        r = a - (q * b)

        print(a, "=", q, "*", b, "+", r)
        if r == 0:
            p = False
        else:
            a = b
            b = r

    print("\nThe greatest common divisor (GCD) of", aa, "and", bb, "is", b)
    t = aa // b
    e = bb // b

    print(aa, "=", b, "*", t)
    print(bb, "=", b, "*", e)


main()