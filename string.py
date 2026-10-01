''''Strings are sequences of characters. 
They can be defined using single quotes, double quotes, or triple quotes. 
Strings can be concatenated using the + operator and can be converted to other 
data types using built-in functions like str().'''

greeting = "Hello, World!"
#print(greeting)

#print(greeting[0])  # Accessing the first character of the string
#print(greeting[7:12])  # Slicing the string to get "World"
#print(len(greeting))  # Getting the length of the string
#print(greeting [-1])  # Accessing the last character of the string

greeting = greeting * 3  # Repeating the string three times
#print(greeting)

name = "Koren"
age = 21

#name_and_age = name + ' ' + str(age)
#print(name_and_age)


#name_and_age = name
#name_and_age += str(age)  # Concatenating name and age using the += operator
#print(name_and_age)  # Output: Koren 21

name_and_age = f"My name is {name} and I am {age} years old."  # Using f-strings for string formatting
print(name_and_age)  # Output: My name is Koren and I am 21

num1 = 777
num2 = 3
print(f"The sum of {num1} and {num2} is {num1 + num2}.")  # Output: The sum of 777 and 3 is 780.
