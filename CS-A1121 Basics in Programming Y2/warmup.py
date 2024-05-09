def names_from_file(filename):
    """
    Return a list of strings that are read from __filename__-file.

    PARAMETERS:
    filename (string) : name of the file to read strings from
    """

    list = []
    try:
        namefile = open(filename, "r")
        for line in namefile:
            line = line.rstrip()
            list.append(line)

        namefile.close()

    except OSError:
        print("Error in reading {:s} file.".format(filename))

    print(list)
    return list


def correct_string(string, symbols):
    """
    Return a new string which is __string__ without characters that are in __symbols__-list.
    You can assume that every item in __symbols__ are one character long.

    PARAMETERS:
    string (string) : a string of characters
    symbols (list) : a list of characters

    EXAMPLE:
    correct_string( "a!b?c%d/ef" , ["%","!","?","/"] )
    returns "abcdef".
    """
    list = []
    for i in string:
        if i not in symbols:
            list.append(i)

    return ''.join(list)


def count_weighted_average(courses):
    """
    Return a weighted average* of courses from given 2-dimensional list __courses__.
    Average is zero if there are no courses in __courses__-list.
    *Weighted average is counted: sum of grade*credits from all courses / sum of all credits

    PARAMETERS:
    courses (2-dimensional list) : A list of courses. One course is a 3 item list: [grade, coursename , credits]

    EXAMPLE:
    count_weighted_average( [[5, "Basics in Programming Y1", 5], [2, "Communicating Technology", 3],[3, "Fourier Analysis", 5]] )
    returns 3.5384615384615383
    """
    sumgrade = 0
    sumcredits = 0
    if courses:
        for line in courses:
            sumgrade += (line[0] * line[2])
            sumcredits += line[2]

        return sumgrade / sumcredits
    return 0


def find_student(dictionary, info):
    """
    Search __info__ from __dictionary__ values and returns the dictionary key of __info__.
    If __info__ is not in dictionary return False.

    PARAMETERS:
    dictionary (dictionary) : string points to 2-dimentional list
    info (2-dimensional list) : __courses__-list from count_weighted_average

    EXAMPLE:
    dictionary = { "Tiina Teekkari" : info1, "Teemu Teekkari": info2, "Kaisa Kemisti": info3 , "Kalle Kemisti": info4 }

    find_student(dictionary, info2)
    returns "Teemu Teekkari"
    """
    for name, inf in dictionary.items():
        if inf == info:
            return name

    return False


def is_on_course(students, participants):
    """
    Return a list of strings that are on both __students__-list and __participants__list, and the lenght of the new list.

    PARAMETERS:
    students (list) : list of strings
    participants (list) : list of strings

    RETURNS:
    a list, a lenght of the list (int)

    EXAMPLE:
    students = ["Tiina Teekkari", "Teemu Teekkari", "Kaisa Kemisti", "Kalle Kemisti"]
    participants = ["Anni Arkkitehti", "Antti Arkkitehti", "Teemu Teekkari", "Kaisa Kemisti"]

    is_on_course(students,participants)
    returns ["Teemu Teekkari", "Kaisa Kemisti"], 2
    """
    list = []

    for i in students:
        if i in participants:
            list.append(i)

    return list, int(len(list))
