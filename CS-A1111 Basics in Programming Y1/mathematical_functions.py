def f(a):
    return 2 * a + 5

def g(a):
    return -2 * a**2 + 5 * a + 10

def h(a):
    if a < 4:
        return 2 * a
    else:
        return 0.5 * a + 6

def reciprocal(a):
    if a == 0:
        return None
    else:
        return 1 / a

def main():
    x = float(input("Enter a value for x:\n"))
    print("x =", x)
    print("f(",x, ") =", f(x))
    print("g(",x, ") =", g(x))
    print("h(",x, ") =", h(x))
    if reciprocal(x) is not None:
        print("The reciprocal of", x, "is equal to", reciprocal(x))
    else:
        print("The number 0.0 has no reciprocal")

main()