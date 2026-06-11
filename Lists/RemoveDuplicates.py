numbers = [10, 25, 5, 10, 15, 25, 10]

if not numbers:
    print("List is Empty")
else:
    dedupe_list = []
    for num in numbers:
        if num not in dedupe_list:
            dedupe_list.append(num)
            
    print(dedupe_list)