import csv
import webbrowser


def number8():
    '''Explore more information regarding numerology: (Press y/n) '''
    print("\nFollowing students' birth date sums total 8\n")

    with open('Student-Icard.csv', 'r') as csv_file:
        csv_re = csv.reader(csv_file)

        print("Srno.\tRollno.\t Birth Date\tName")
        next(csv_re)  # skips all columns' heading

        list_of_csv = list(csv_re)  # taking data as a 2D list
        cnt = 0
        for idx, row in enumerate(list_of_csv):  # idx -> roll number
            row8 = row[8]

            # tens place + units place
            add2 = int(str(row8)[:1]) + int(str(row8)[1:2])

            if(add2 == 8):  # principle condition
                cnt += 1
                print(" ", cnt, "\t", idx, "\t", row[8], "\t", row[2])

    print(number8.__doc__)
    if(input('') == 'y'):
        webbrowser.open(
            "https://astrotalk.com/numerology-introduction/numerology-number-8")
    else:
        print("COOL! Even my birth date sums total 8")


if __name__ == "__main__":
    number8()
