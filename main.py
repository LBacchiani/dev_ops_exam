# Copyright (c) 2023 Lorenzo Bacchiani
# All rights reserved.

from my_fibonacci import fibonacci
from prime_numbers import prime_numbers

def main(function_name, number):
    if function_name == "-p":
        result = prime_numbers(number)
        print(f"Prime numbers up to {number}: {result}")
    elif function_name == "-f":
        result = fibonacci(number)
        print(f"Fibonacci sequence up to {number}: {result}")
    else:
        print("Invalid function name. Please provide either '-p' or '-f'.")

if __name__ == "__main__":
    function_name = input("Enter the name of the function to invoke (-p or -f): ")
    number = int(input("Enter a number: "))
    main(function_name, number)