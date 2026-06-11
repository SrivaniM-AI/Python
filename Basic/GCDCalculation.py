number1 = int(input("Give your first number"))
number2 = int(input("Give your second number"))

smallest = number1 if number1 <= number2 else number2
    
while smallest > 0:
    if number1 % smallest == 0 and number2 % smallest == 0:
        print(f"GCD of given two numbers {number1} and {number2} is: {smallest}")
        break
    smallest -= 1
    
#Euclidean Alg:
while number2 != 0:
    number1, number2 = number2, number1 % number2
    print(f"{number1}, {number2}")
print(f"Gcd is {number1}")
    
