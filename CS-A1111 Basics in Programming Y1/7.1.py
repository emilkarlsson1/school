

def main():
    filename = input("Enter the name of the file to be read:\n")
    try:
        product_file = open(filename,'r')
        total = 0.0
        optimal = 0
        allowed = 0
        faulty = 0
        count = 0
        for line in product_file:
            line = line.rstrip()
            measure = float(line)
            if 4.52 <= measure <= 4.58:
                optimal += 1
            elif 4.50 <= measure <= 4.60:
                allowed += 1
            else:
                faulty += 1
            total += measure
            count += 1
        product_file.close()

        opt = (optimal / count) * 100
        al = (allowed / count) * 100
        fault = (faulty / count) * 100

        print("File read succesfully.")
        if count == 0:
            print("The file didn't contain any data.")
        else:
            print("The batch contained:\n{:d} optimal ({:.1f}%)\n"
                  "{:d} allowed ({:.1f}%)\n{:d} faulty ({:.1f}%).".format(optimal, opt, allowed, al, faulty, fault))

        if fault > 3.0:
            print("The batch didn't pass the quality inspection.")
        else:
            print("The batch passed the quality inspection.")

    except OSError:
        print("Error in reading the file '{:s}'. Program ends.".format(filename))
    except ValueError:
        print("Incorrect number in the file '{:s}'. Program ends.".format(filename))

main()
