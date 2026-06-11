numbers = [10, 25, 5, 40, 15]

if not numbers:
    print("List is empty")
else: 
    Largest = numbers[0]
    for number in numbers:
        if number > Largest:
            Largest = number

print(f"Largest Number in the list is: {Largest}")

Largest = numbers[0]
[Largest:= number for number in numbers if number > Largest]
print(f"Largest Number in the list is: {Largest}")
