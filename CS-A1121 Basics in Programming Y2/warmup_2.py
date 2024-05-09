import course
from student import Student
from course import Course


def create_students(filename):
    """
    Reads a text file containíng student information, 
    and creates Student-objects based on the contents.
    Name of the file to be read is given as the parameter.
    Each correct row of the file has a name and a student number separated by a slash ('/').
    If a row is correct, a new Student-object is created with that name and student number.
    Incorrect rows, i.e. rows that do not have a string and an integer separated by a slash,
    are skipped.
    Finally the function returns a list of all created Student-objects.
    """

    lista = []
    try:
        file = open(filename, 'r')
        for line in file:
            line = line.rstrip()
            line = line.split('/')
            name = line[0]
            if len(line) == 2:
                try:
                    num = int(line[1])
                    new = Student(name, num)
                    lista.append(new)
                except ValueError:
                    print("ValueError")

        file.close()
    except ValueError:
        print("ValueError")

    return lista

def add_courses(filename, student):
    """
    Reads a text file containing course information,
    creates Course-objects based on the contents, and adds them
    to the completed courses of the student given as the second parameter.
    Name of the file to be read is given as the first parameter.
    Each correct row of the file has the name of the course and its credits
    separated by a comma (','). Incorrect rows, i.e. rows that do not have a string
    and an integer separated by a comma, are skipped.
    Credits for a course should be in the range 1-15.
    Function returns the amount of courses successfully added for the student.
    """
    lista = []
    try:
        file = open(filename, 'r')
        for line in file:
            line = line.rstrip()
            line = line.split(',')
            if len(line) == 2 and 1 <= int(line[1]) <= 15:
                lista.append(line)

        file.close()
    except ValueError:
        print("ValueError")
    i = 0
    for line in lista:
        olio = Course(line[0], int(line[1]))
        student.add_course(olio)
        i += 1

    return i


def compare_student_numbers(student1, student2):
    """
    Compares two given Student-objects, student1 and student2, and returns the one with a smaller id.

    EXAMPLE:
    given objects:
    student1, id: 123456
    student2, id: 234567

    compare_student_numbers(student1, student2):
    returns: student1
    """

    id1 = student1.get_id()
    id2 = student2.get_id()
    if id1 > id2:
        return student1
    else:
        return student2


def get_credits(student):
    """
    Calculates and returns the sum of credits of all the courses the student has completed.
    """

    lista = student.get_courses()
    sum = 0
    for line in lista:
        sum += int(line.get_credits())

    return sum

def compare_credits(student1, student2):
    """
    Compares two students total credits. Returns the student with the highest credit count.
    Use the function get_credits to get the total credits. 
    If both students have an equal amount of credits, the function returns 0.
    """

    eka = get_credits(student1)
    toka = get_credits(student2)
    if eka > toka:
        return student1
    elif eka == toka:
        return 0
    else:
        return student2


def main():
    filename = input("Enter the name of the student file\n")
    student_list = create_students(filename)

    for student in student_list:
        filename = input("Enter the name of the course file\n")
        courses = add_courses(filename, student)
        print("{:d} courses added for {:s}".format(courses, student.get_name()))

    for student in student_list:
        print("{:s} has {:d} credits".format(student.get_name(), get_credits(student)))

    print(compare_credits(student_list[0], student_list[1]))
    #TODO: Write your own code for testing if the called functions worked

if __name__ == "__main__":
    main()

