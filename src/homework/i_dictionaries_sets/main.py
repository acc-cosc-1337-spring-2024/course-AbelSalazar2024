#HW6 main program

import dictionary

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