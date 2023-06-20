def prime_numbers(n):
    def is_prime(num, divisor=2):
        if num <= 1:
            return False
        elif divisor * divisor > num:
            return True
        elif num % divisor == 0:
            return False
        else:
            return is_prime(num, divisor + 1)

    return [num for num in range(2, n + 1) if is_prime(num)]