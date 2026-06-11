numbers = [10, 25, 5, 10, 15, 25, 10]

if not numbers:
    print("List is Empty")
else:
    unique_items = []
    frequency_count = []
    
    for num in numbers:
        if num not in unique_items:
            unique_items.append(num)
            frequency_count.append(1)
        else:
            index = unique_items.index(num)
            frequency_count[index] += 1
            
    for i in range(len(unique_items)):    
        print(f"{unique_items[i]} -> {frequency_count[i]}")