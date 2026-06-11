a , b, c = 10, 30, 20

def findMax(a, b, c):
    if a >= b and a >= c:
        print(f"Largest Number is: {a}")
    elif b >= a and b >= c:
        print(f"Largest Number is: {b}")
    else:
        print(f"Largest Number is: {c}")

def findSmallestLargestMiddle(a , b, c):
    largest, smallest = a, a
    if b > largest:
        largest = b
    if c > largest:
        largest = c
    if b < smallest:
        smallest = b
    if c < smallest:
        smallest = c
    middle = a+b+c-largest-smallest
    print(f"Largest {largest}")
    print(f"Smallest: {smallest}")
    print(f"Middle: {middle}")



findMax(5,5,5)

findMax(10, 15, 11)

print(max(12, 13, 15))

findSmallestLargestMiddle(10, 34, 23)