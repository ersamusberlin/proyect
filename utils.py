# utils.py
import validator

def get_number(prompt):
    value = input(prompt)
    while not validator.is_number(value):
        print("Invalid number, try again.")
        value = input(prompt)
    return float(value)
