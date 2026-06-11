def is_prime(number):
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False 
    for i in range(3, int(number ** 0.5) + 1, 2):
        if number % i == 0:
            return False
    return True

def count_primes(numbers):
    counter = 0
    for i in numbers:
        if is_prime(i):
            counter += 1
    return counter

print(count_primes([2, 3, 4, 5, 6, 7, 8]))
print(count_primes(range(10)))