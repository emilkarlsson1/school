import datetime


def convert_date_text_to_datetime_object(date_as_text):
    "Returns a datetime.date object converted from string 'date_as_text'."
    date_as_list = date_as_text.split(".")
    day, month, year = [int(part) for part in date_as_list]
    return datetime.date(year, month, day)


def print_file_contents(name_of_the_file):
    "Prints the contents of the file with the name 'name_of_the_file'. Make sure the file is not still open elsewhere before calling this function."
    file = open(name_of_the_file, 'r')
    line = file.readline()
    while line != '':
        print(line, end='')
        line = file.readline()
    file.close()


def main():
    filename = input("Enter the name of the file to be created for your screen time data:\n")
    file = open(filename, 'w')
    date_text = input("Enter the start date in format 'DD.MM.YYYY':\n")
    date_text = date_text.split('.')
    yer = int(date_text[2])
    mon = int(date_text[1])
    da = int(date_text[0])
    paiv = datetime.date(yer, mon, da)
    print("Enter your screen watching time for each day (in minutes) in the format '[Phone minutes]"
          " [PC minutes] [TV minutes] [other minutes]'")

    count = 0
    tilos = 0
    mins = []
    rivi = input("Enter your screen time on {}: ".format(paiv))
    while rivi != "":

        mins.append(rivi)
        sli = rivi.split(" ")
        eka = int(sli[0])
        toka = int(sli[1])
        ko = int(sli[2])
        ne = int(sli[3])
        file.write("{}: {:d}/{:d}/{:d}/{:d}".format(paiv, eka, toka, ko, ne))
        tilos += eka + toka + ko + ne
        count += 1
        paiv = datetime.date(yer, mon, da) + datetime.timedelta(days=count)

        rivi = input("Enter your screen time on {}: ".format(paiv))
        file.write("\n")
    file.close()
    print("-" * 100)
    print("Screen times saves succesfully in the file '{:s}'".format(filename))
    print("Saved the screen times of {:d} days.".format(count))

    if count != 0:
        kesk = tilos / 60
        daavg = kesk / count
        print("Total screen time from this period is {:.1f} hours and daily average is {:.1f} hours.".format(kesk, daavg))


    print()
    print("Let's look inside the file. It looks as follows:")
    print("-" * 100)

    print_file_contents(filename)


main()