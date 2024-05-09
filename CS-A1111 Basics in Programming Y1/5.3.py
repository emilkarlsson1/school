def prime_factorize(number):

    i = 2
    lista = []

    while i <= number:

        jako = number % i
        if jako == 0:
            number /= i
            lista.append(i)
        else:
            i += 1

    return lista


def main():
    num = int(input("Enter the number to be prime-factorized:\n"))
    result = prime_factorize(num)
    print("prime_factorize({:d}) returned {}".format(num, result))
    print("Meaning that the prime factorization of {number:d} is\n{number:d} == {factors_string}."
          .format(number = num, factors_string = " * ".join( str(factor) for factor in result) ))
main()