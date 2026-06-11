def largest(numbers):
    if not numbers:
        return None
    
    largest = numbers[0]
    for num in numbers[1:]:
        if num > largest:
            largest = num
    return largest

print(largest([1,2,3,4,5]))
print(largest([]))