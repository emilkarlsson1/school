# Y1 SUMMER 2020
# Basic Course in Programming Y1
# Author: Joel Lahenius
# Template for exercise 5.2 months

MONTHS_FI = ["tammikuu", "helmikuu", "maaliskuu", "huhtikuu", 
             "toukokuu", "kesakuu", "heinakuu", "elokuu", 
             "syyskuu", "lokakuu", "marraskuu", "joulukuu"]
MONTHS_EN = ["January", "February", "March", "April",
             "May", "June", "July", "August",
             "September", "October", "November", "December"]

LANGUAGE_FI = 1
LANGUAGE_EN = 2

def num_to_month(num, language):
    """
    Returns a string resembling the given month in given language, or "" is num is not in range 1...12.
    1 corresponds to January and 12 to December.
    
    You can assume the language parameter is valid.
    
    Parameters:
    num: int
    language: a LANGUAGE_XX constant, where XX resembles the language
    
    returns: str
    """
    x = num - 1
    # write your code here
    if x > -1:
        if x < 12:
            if language == 1:
                return MONTHS_FI[x]
            else:
                return MONTHS_EN[x]
        else:
            return ""
    else:
        return ""


def month_to_num(month, language):
    """
    Returns the number of given month in given language, or -1 if the month is not found.
    NOTE: Returning negative numbers to resemble errors is NOT a good practise,
    but we are not familiar with raising and handling errors this early in the course.
    
    You can assume the language parameter is valid.
    
    Parameters:
    month: str
    language: a LANGUAGE_XX constant, where XX resembles the language
    
    returns: int
    """
    
    # write your code here

    if language == 1:
        i = 0
        p = True
        while p:
            if MONTHS_FI[i] != month:
                if i < 11:
                    i += 1
                else:
                    i = 133
                    p = False
            else:
                p = False

        if i < 12:
            return i + 1
        else:
            return -1
    else:
        i = 0
        p = True
        while p:
            if MONTHS_EN[i] != month:
                if i < 11:
                    i += 1
                else:
                    i = 133
                    p = False
            else:
                p = False

        if i < 12:
            return i + 1
        else:
            return -1

CONVERT_NUM_TO_MONTH = 1
CONVERT_MONTH_TO_NUM = 2
QUIT = 3
POSSIBLE_CHOICES = (CONVERT_NUM_TO_MONTH, CONVERT_MONTH_TO_NUM, QUIT)

def get_user_choice():
    prompt = "Convert...\n(1) ... num to month\n(2) ... month to num\n(3) quit\n"
    choice = int(input(prompt))
    while choice not in POSSIBLE_CHOICES:
        choice = int(input(prompt))
    return choice

def input_integer(prompt, at_least, at_most):
    user_int = int(input(prompt))
    while not at_least <= user_int <= at_most:
        print("Try again, your number should in range {:d}...{:d}".format(at_least, at_most))
        user_int = int(input(prompt))
    return user_int

def input_month_num():
    return input_integer("Month (1...12):\n", 1, 12)
def input_language():
    return input_integer("Language, 1 for Finnish, 2 for English:\n", 1, 2)

def main():
    choice = get_user_choice()
    while choice != QUIT:
        # Note: this section of the code could be better with dictionaries, but it is written this way to keep easy to understand.
        if choice == CONVERT_NUM_TO_MONTH:
            month_num = input_month_num()
            lang = input_language()
            month_text = num_to_month(month_num, lang)
            print("The month is '{:s}'".format(month_text))
        elif choice == CONVERT_MONTH_TO_NUM:
            lang = input_language()
            month = input("Enter the month in that language:\n")
            month_num = month_to_num(month, lang)
            if month_num > 0:
                print("{:s} is the month # {:d}".format(month, month_num))
            else:
                print("Unknown month (according to the function you have written).")
        else:
            print("Unknown choice. Try again.")
        choice = get_user_choice()
    
main()