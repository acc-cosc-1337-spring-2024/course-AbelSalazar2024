#HW2 create and run the main program

import decisions

option = float(input("Enter Option: "))
total = float(input("Enter Total: "))
result = decisions.get_options_ratio(option, total)

print("Ratings: ",decisions.get_faculty_rating(result))


                    