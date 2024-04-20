#HW 7

from class_a import die

die = die()

def menu():
    while True:
        print("1. Roll die")
        print("2. Exit")

        select = input("Select #: ")

        if select == "1":
            die.roll()
            print(die)
        elif select == "2":
            print("Exiting program.")
            break
        else:
            print("Invalid selection. Please enter 1 or 2.")
menu()  