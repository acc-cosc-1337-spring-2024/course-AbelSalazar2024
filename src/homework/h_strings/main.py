#HW5 main program
import strings

while True:
    print("MENU")
    print("1 - Hamming Distance")
    print("2 - DNA Complement")
    print("3 - Exit")

    select = input ("Enter a number 1-3: ")

    if select == '1':
        while True:
            dna1 = input("Enter first DNA string: ")
            dna2 = input("Enter second DNA string: ")
        
            if dna1.isalpha() and dna2.isalpha():
                break
            else:
                print("Invalid input. Enter valid DNA strings.")

        result = strings.get_hamming_distance(dna1, dna2)
        print(f"The Hamming Distance is: {result}")

    elif select == '2':
        while True:
            dna = input("Enter a DNA string: ")

            if dna.isalpha():
                break
            else:
                print("Invalid input. Enter a valid DNA string.")    
            
        result = strings.get_dna_complement(dna)
        print(f"The complementary DNA string is: {result}")

    elif select == '3':
        print("Exiting the program")
        break

    else:
        print("Invalid selection. Please enter a number 1-3.")
        