import operations
import utils

def menu():
    print("\n===== SIMPLE CALCULATOR MADE BY CRISTIAN,ALBERTO, MYKOLA AND NURIA=====")
    print("1) Add")
    print("2) Subtract")
    print("3) Multiply")
    print("4) Divide")
    print("5) Power (a^b)")
    print("6) Square Root")
    print("0) Exit")
    print("=============================")

def run():
    while True:
        menu()
        choice = input("Choose an option: ")

        if choice == "0":
            print("Goodbye!")
            break

        # Operations needing TWO numbers
        if choice in ["1", "2", "3", "4", "5"]:
            a = utils.get_number("Enter first number: ")
            b = utils.get_number("Enter second number: ")

            if choice == "1":
                print("Result:", operations.add(a, b))
            elif choice == "2":
                print("Result:", operations.subtract(a, b))
            elif choice == "3":
                print("Result:", operations.multiply(a, b))
            elif choice == "4":
                print("Result:", operations.divide(a, b))
            elif choice == "5":
                print("Result:", operations.power(a, b))

        # Square root (ONE number)
        elif choice == "6":
            a = utils.get_number("Enter number: ")
            print("Result:", operations.sqrt(a))

        else:
            print("Invalid option, try again.")

run()
