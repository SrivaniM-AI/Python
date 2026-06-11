def find_common_elements(list1, list2):
    set1 = set(list1)
    common = []
    for num in list2:
        if num in set1:
            common.append(num)
    return common

def find_common_elements2(list1, list2):
    set1 = set(list1)
    set2 = set(list2)    
    return list(set1 & set2)

print(find_common_elements([1,2,3,4], [2,3,4,5]))
print(find_common_elements2([1,2,3,4], [2,3,4,5]))