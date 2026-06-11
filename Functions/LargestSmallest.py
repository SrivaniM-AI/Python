def largest_and_smallest(numbers):
    if not numbers:
        return None, None
    largest = smallest = numbers[0]
    for num in numbers[1:]:
        if num > largest:
            largest = num
        elif smallest > num:
            smallest = num
    return largest, smallest

largest, smallest = largest_and_smallest([10, 25, 5, 40, 15])

print(largest)
print(smallest)