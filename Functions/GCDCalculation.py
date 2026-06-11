def calculateGCD(a, b):
    smallest = a if a <= b else b
  
    while smallest > 0:
        if a % smallest == 0 and b % smallest == 0:
            return smallest
        smallest -= 1

print(calculateGCD(12, 18))