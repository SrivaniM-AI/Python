def two_sum(numbers, target):
    seen = {}    
    
    for index, num in enumerate(numbers):
        complement = target - num        
        if complement in seen:
            return seen[complement], index
        else:            
            seen[num] = index
    return None, None
        
print(two_sum(numbers=[2,8,9,7,1,11,0], target=9))
        
    
