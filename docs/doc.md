# My Project

This project includes three Python files: `my_fibonacci.py`, `prime_numbers.py`, and `main.py`. These files provide functionalities related to the Fibonacci sequence and prime numbers.

## Fibonacci Function

The `my_fibonacci.py` file contains the `fibonacci` function, which takes a parameter `n` and outputs the Fibonacci sequence from 0 to `n`. The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones.

To use the `fibonacci` function, import it into your code and call it with the desired value of `n`. For example:

```python
from my_fibonacci import fibonacci

n = 10
sequence = fibonacci(n)
print(sequence)
```

## Prime Number Function

The prime_numbers.py file contains a Python function called prime_numbers. This function takes a parameter n and outputs the sequence of prime numbers from 0 to n. Prime numbers are numbers greater than 1 that have no divisors other than 1 and themselves.

To use the prime_numbers function in your own code, you can import it as follows:

```python
from prime_numbers import prime_numbers

n = 20
sequence = prime_numbers(n)
print(sequence)
```

## Main

The main.py file serves as the entry point for the program and provides a command-line interface for the user. It prompts the user for the function to invoke (-f for Fibonacci or -p for prime numbers) and the value of n.

```
python main.py
```

The program will prompt you for the function choice and n value.

