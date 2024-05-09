def main():
    amount = int(input("How many products are you going to input?\n"))
    prices = [0.0] * amount
    for i in range(amount):
        inputted_price = float(input("Enter the price of the next product (eur).\n"))
        prices[i] = inputted_price

    print("Discount prices")
    i = 0
    sum = 0
    while i < amount:
        if prices[i] < 50.0:
            sum += prices[i] * 0.9
            print("{:.2f} eur".format((prices[i] * 0.9)))
            i += 1
        else:
            sum += prices[i] * 0.7
            print("{:.2f} eur".format((prices[i] * 0.7)))
            i += 1
    print("Sum of discount prices: {:.2f} eur.".format(sum))
main()