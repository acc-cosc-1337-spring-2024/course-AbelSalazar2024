#HW7 main program

import sets

prog1 = {'Student1', 'Student2', 'Student3'}
prog2 = {'Student3', 'Student4', 'Student5'}

while True:
    print("1-Students who took prog1 and prog2")
    print("2-Students who took prog2 only")
    print("3-Students who took prog1 not prog2")
    print("4-Students who took prog2 not prog1")
    print("5-Exit")

    select = input("Enter your selection: ")

    if select == '1':
        print("Students who took prog1 and prog2:", sets.get_students_who_took_prog1_and_prog2(prog1, prog2))
    elif select == '2':
        print("Students who took prog2 only:", sets.get_students_who_took_prog2_only(prog1, prog2))
    elif select == '3':
        print("Students who took prog1 not prog2:", sets.get_students_who_took_prog1_not_prog_2(prog1, prog2))
    elif select == '4':
        print("Students who took prog2 not prog1:", sets.get_students_who_took_prog2_not_prog_1(prog1, prog2))
    elif select == '5':
        print("Exiting the program.")
        break
    else:
        print("Invalid selection. Please enter a number between 1-5.")

"""
HW6 - main program
inventory = {}
while True:
    
    print("1 - Add or Update Item")
    print("2 - Delete Item")
    print("3 - Exit")

    select = input("Enter a number 1-3: ")

    if select == "1":
        widget_name = input("Enter the widget name: ")
        quantity = int(input("Enter the quantity: "))
        dictionary.add_inventory(inventory, widget_name, quantity)            
        print(f"{quantity} {widget_name}(s) added/updated in inventory.")
    
    elif select == "2":
        widget_name = input("Enter the widget name to delete: ")
        result = dictionary.remove_inventory_widget(inventory, widget_name)
        print(result)
    
    elif select == "3":
        print("Exiting the program. ")
        break

    else:
        print("Invalid selection. Please select 1-3: ")
"""