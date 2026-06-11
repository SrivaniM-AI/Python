number = int(input('Give your number'))
original_number = number

num_digits = 0

if number == 0:
    num_digits = 1
else:
    while number > 0:
        number = number // 10
        num_digits += 1

num_total = 0
number = original_number

while number > 0:
    num_total += (number % 10)**num_digits
    number = number // 10

if original_number == num_total:
    print(f"Given Number {original_number} is Armstrong")
else:
    print("Not Armstrong")



