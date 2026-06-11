def find_first_duplicate(numbers):
    seen = set()
    for num in numbers:
        if num in seen:
            return num
        seen.add(num)
    return None     
        
print(find_first_duplicate([1,2,3,4,5,1,2,3,4,5]))