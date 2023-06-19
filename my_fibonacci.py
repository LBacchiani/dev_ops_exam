def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib = fibonacci(n-1)
        next_number = fib[-1] + fib[-2]
        fib.append(next_number)
        return fib
