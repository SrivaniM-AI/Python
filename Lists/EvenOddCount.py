numbers = [10, 25, 5, 40, 15]

if not numbers:
    print("List is Empty")
else:
    even_count = 0
    odd_count = 0
    for num in numbers:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    print(f"Count of Even numbers {even_count}")
    print(f"Count of Odd numvers: {odd_count}")