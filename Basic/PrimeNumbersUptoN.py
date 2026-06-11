import math

number = int(input("Give your Number"))
prime_list = []

if number <= 1:
    print(f"No Prime Numbers")
elif number == 2:
    print(f"Prime Numbers: {2}")
else:  
    prime_list.append(2)  
    for i in range(3, number+1, 2):
        num = int(math.sqrt(i))
        for j in range(3, num+1, 2):
            if i % j == 0:
                break
        else:
            prime_list.append(i)

print(*prime_list)
            
        


    

    