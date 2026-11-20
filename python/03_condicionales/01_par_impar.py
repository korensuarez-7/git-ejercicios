print("/////////////////////////////////////")
name = input("Please enter your name: ")
print(f"Hello, {name}!")
num1= int(input("Please enter the first number: "))
num2= int(input("Please enter the second number: "))

if num1 % 2 == 0:
    print(f"{num1} is an even number.")
else:
    print(f"{num1} is an odd number.")

if num2 % 2 == 0:
    print(f"{num2} is an even number.")
else:
    print(f"{num2} is an odd number.")

if num1 > num2:
    if num1 % 2 == 0:
        print(f"{num1} is greater than {num2} and it is an even number.")
    else:
        print(f"{num1} is greater than {num2} but it is an odd number.")
else:
    print(f"{num1} is not greater than {num2}.")