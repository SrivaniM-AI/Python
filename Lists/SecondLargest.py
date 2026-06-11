numbers = [5,5,4]

# with distinct second largest element
if len(numbers) < 2:
    print(f"List doesn't have second element")
else:
    largest = float('-inf')
    second_largest = float('-inf')
    
    for num in numbers:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    
    if second_largest == float('-inf'):
        print("No second largest distinct element")
    else:   
        print(f"Second Largest in the given list is {second_largest}")
        
#with out distinct
if len(numbers) < 2:
    print("No second element in the list")
else:
    largest = float('-inf')
    second_largest = float('-inf')
    for num in numbers:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest:
            second_largest = num
    print(f"Second Largest in the given list is {second_largest}")
        
