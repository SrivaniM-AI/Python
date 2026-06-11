numbers = [10, 25, 5, 40, 15]

if not numbers:
    print("List is Empty")
else:
    largest = smallest = numbers[0]
    for num in numbers[1:]:
        if num > largest:
            largest = num
        elif num < smallest:
            smallest = num            
    print(f"Largest Number is: {largest}")
    print(f"Smallest Number is: {smallest}")
    