numbers = [10, 25, 5, 10, 15, 25, 10]

if not numbers:
    print("List is Empty")
else:
    reverse_list = []
    i = len(numbers) - 1
    while i >= 0:
        reverse_list.append(numbers[i])
        i -= 1
            
    print(reverse_list)
    
    # using for
    reverse_list = []
    for i in range(len(numbers) -1, -1, -1):
        reverse_list.append(numbers[i])        
    print(reverse_list)
