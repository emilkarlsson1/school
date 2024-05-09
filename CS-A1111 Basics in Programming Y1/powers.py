def main():
    base = int(input("Base number:\n"))
    limit = int(input("Upper limit for the powers:\n"))
    tulos = 0
    i = 1
    print("Powers:")
    while tulos <= limit:
        a = base ** i
        if a <= limit:
            print(a)
            i += 1
            tulos = a
        else:
            i += 1
            tulos = a
main()