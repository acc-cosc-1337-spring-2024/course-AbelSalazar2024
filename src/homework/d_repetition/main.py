#HW 3 create menu
import repetition

while True:
    print("MENU")
    print("1 - Factorial")
    print("2 - Sum odd numbers")
    print("3 - Exit")

    select = input("Enter a number 1-3: ")

    if select == '1':
        user_sel = -1

        while not (user_sel >= 0 and user_sel <= 10):
            user_sel = int(input("Enter a number between 0 and 10: "))
            if not (user_sel >= 0 and user_sel <= 10):
                print("Please enter a valid number.")
        
        print("Factorial of", user_sel, "is", repetition.get_factorial(user_sel))
            
    elif select == '2':
        user_sel = -1
        
        while not (user_sel >= 0 and user_sel <= 100):
            user_sel = int(input("Enter a number between 0 and 100: "))
            if not (user_sel >= 0 and user_sel <= 100):
                print("Please enter a valid number.")
        
        print("Sum of odd numbers up to", user_sel, "is", repetition.sum_odd_number(user_sel))

    elif select == '3':
        exit_sel = input("Do you want to exit? (Y/N): ")
        if exit_sel == "Y":
            print("Exiting the program. ")
            break
        
    else:
            print("Invalid selection. Please enter a number 1-3.")
         
    