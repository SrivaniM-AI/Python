numbers = [1, 2, 3, 4, 5]

is_sorted = True

for i in range(len(numbers) - 1):
    if numbers[i] > numbers[i + 1]:
        is_sorted = False
print(f"Array is sorted: {is_sorted}")
    