def contains_duplicates(numbers):
    return len(numbers) != len(set(numbers))        

print(contains_duplicates([1,2,3]))