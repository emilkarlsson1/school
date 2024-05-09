import random

RED = [3,3,3,3,3,6]
BLUE = [2,2,2,5,5,5]
OLIVE = [1,4,4,4,4,4]
DICE_NAMES = ["Red", "Blue", "Olive"]

# The function initialises the random number generator
# with the seed number input by the user.


def init_die():
    siemenluku = int(input("Give a seed for the dice.\n"))
    random.seed(siemenluku)

# IMPLEMENT THE MISSING FUNCTIONS HERE


def roll(die):
    if die == 0:
        r = random.randint(0, 5)
        return RED[r]
    elif die == 1:
        r = random.randint(0, 5)
        return BLUE[r]
    elif die == 2:
        r = random.randint(0, 5)
        return OLIVE[r]


def simulate_singles(die1, die2, rolls):

    d1 = 0
    d2 = 0
    ts = 0
    i = 0
    y = 0
    x = 0

    while i < rolls:
        y = roll(die1)
        x = roll(die2)
        if y > x:
            d1 += 1
        elif y < x:
            d2 += 1
        elif y == x:
            ts += 1
        y = 0
        x = 0
        i += 1

    return d1, d2, ts


def simulate_doubles(die1, die2, rolls):

    i = 0
    d1 = 0
    d2 = 0
    ts = 0
    y = 0
    x = 0

    while i < rolls:
        y += roll(die1)
        y += roll(die1)

        x += roll(die2)
        x += roll(die2)
        if y > x:
            d1 += 1
        elif y < x:
            d2 += 1
        elif y == x:
            ts += 1
        y = 0
        x = 0
        i += 1

    return d1, d2, ts


# Calls for the appropriate simulation function
# and prints the outcome of the simulation.


def simulate_and_print_result(die1, die2, rolls, simulation_function, header):
    wins1, wins2, draws = simulation_function(die1, die2, rolls)
    print(header)
    print("Player 1 used {:s} die and won {:d} times, so {:.1f}% of the rolls.".format(DICE_NAMES[die1],wins1,wins1/rolls*100))
    print("Player 2 used {:s} die and won {:d} times, so {:.1f}% of the rolls.".format(DICE_NAMES[die2],wins2,wins2/rolls*100))
    if draws != 0:
        print("{:d} draws, so {:.2f}% of the rolls.".format(draws, draws/rolls*100))


def main():
    print("Welcome to a non-transitive dice simulation.")
    init_die()
    print("The dice:")
    print("{:d} for {:s}: {:}".format(0 ,DICE_NAMES[0], RED))
    print("{:d} for {:s}: {:}".format(1 ,DICE_NAMES[1], BLUE))
    print("{:d} for {:s}: {:}".format(2 ,DICE_NAMES[2], OLIVE))

    choice1 = int(input("Choose a die for player 1:\n"))
    choice2 = int(input("Choose a die for player 2:\n"))
    rolls = int(input("How many rolls to simulate?\n"))
    simulate_and_print_result(choice1, choice2, rolls, simulate_singles, "Singles:")
    simulate_and_print_result(choice1, choice2, rolls, simulate_doubles, "Doubles:")


main()
