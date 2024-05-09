def enter_values(dictionary, name, step_input):
    # Implement your code here
    y = step_input.split(",")
    if name in dictionary:
        for x in range(0, len(y)):
            dictionary[name].append(y[x])
    else:
        dictionary[name] = step_input.split(",")


def search_by_name(dictionary, name):
    # Implement your code here
    if name in dictionary:
        a = []
        askel = 0
        for nam in dictionary[name]:
            osa = int(nam)
            a.append(osa)
            askel += osa
        return a, askel
    else:
        return [], -1


def main():
    dictionary = {}

    name = input("Enter the name of the person. Stop with an empty line.\n")
    while name != "":
        step_input = input("Enter the different day's steps on one line.\n")
        enter_values(dictionary, name, step_input)
        name = input("Enter the name of the person. Stop with an empty line.\n")

    name = input("Enter name to search. Stop with an empty line.\n")
    while name != "":
        step_list, total_steps = search_by_name(dictionary, name)
        if total_steps == -1:
            print("No information on that person.")
        else:
            print("{:s}'s steps in a list: {}".format(name,step_list))
            print("{:s}'s total steps: {:d}".format(name,total_steps))
        name = input("Enter name to search. Stop with an empty line.\n")

    # print(dictionary)
    '''
    Remove the hash character from the line above if you want to see
    the contents of the dictionary while testing your program.
    Comment it back when you return your program.
    '''
    print("Program ends.")

main()