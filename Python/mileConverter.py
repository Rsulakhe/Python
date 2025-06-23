
from math import isclose
mile = int(input("Enter the distance in miles: "))

km = mile * 1.60934
print("The distance in kilometers is:", km)


age, name = 30, 'Rock'

print(f"{name} is {age} years old.")
# Using f-string for formatted output


x = 6 + 3  # -3;
print(f"The value of x is: {x}")


a = 9
b = 2

Distance_miles = 2806
Distance_km = Distance_miles * 1.60934
print(f"The distance in kilometers is: {Distance_km}")

tempatrue_celsius = 25
tempatrue_fahrenheit = (tempatrue_celsius * 9/5) + 32
print(f"The temperature in Fahrenheit is: {tempatrue_fahrenheit}")

inch = 17
centimeter = inch * 2.54

year_in_seconds = 60 * 60 * 24 * 365
print(f"One year has {year_in_seconds} seconds.")

a = 5

# plus equals operator
a += 3  # stands for shorthand for a = a + 3
print(f"The value of a after plus equals operator is: {a}")

# minus equals operator
a -= 2  # stands for shorthand for a = a - 2
print(f"The value of a after minus equals operator is: {a}")

# multiply equals operator
a *= 4  # stands for shorthand for a = a * 4
print(f"The value of a after multiply equals operator is: {a}")

# divide equals operator
a /= 2  # stands for shorthand for a = a / 2
print(f"The value of a after divide equals operator is: {a}")

# double stars operator
a **= 2  # stands for shorthand for a = a ** 2
print(f"The value of a after double stars operator is: {a}")

# modulus equals operator
a %= 3  # stands for shorthand for a = a % 3
print(f"The value of a after modulus equals operator is: {a}")

# divmod
a, b = divmod(10, 3)  # returns a tuple (quotient, remainder)
print(f"The quotient is: {a}, and the remainder is: {b}")

# pow
a = pow(2, 3)  # returns 2 raised to the power of 3
print(f"2 raised to the power of 3 is: {a}")

# sum
print(sum([1, 2, 3, 4, 5]))  # returns the sum of the list

# max
print(max([1, 2, 3, 4, 5]))  # returns the maximum value in the list

# min
print(min([1, 2, 3, 4, 5]))  # returns the minimum value in the list

# round
print(round(3.14159, 2))  # rounds the number to 2 decimal places
a = 7.864541266543343
print(round(a, 2))  # rounds the number to 3 decimal places


# Immutable vs Mutable Types
# Immutable types: int, float, str, tuple,frozenset

# Mutable types: list, set, dictonary

# Example of immutable type
x = 5
print(id(x))  # Different id after modification
print(f"Original x: {x}")
x += 2  # This creates a new integer object
print(id(x))  # Different id after modification

# Example of mutable type
my_list = [1, 2, 3]
print(id(my_list))  # Original id
my_list.append(4)  # Modifies the original list
print(id(my_list))  # Same id after modification

a = 5
a **= 2  # output: 25
a /= 5  # output: 5.0

name = "marry"
id1 = id(name)
name = "john"
id2 = id(name)

id1 == id2\

a, b, c, d, = 2, 4, 6, 8

d != - b  # output: True

print(format(1/3, '.30f'))  # output: 0.3333333333333333

a = 0.1 * 5
b = 0.5
print(a == b)  # output: False, due to floating-point precision issues
# output: True, using isclose to compare floating-point numbers
print(isclose(a, b))

a = 10
b = 4.568
isClose = True
name = "Rock"
emp = ["John", "Doe", "Jane"]

print(type(a))  # output: <class 'int'>
print(type(b))  # output: <class 'float'>
print(type(isClose))  # output: <class 'bool'>
print(type(name))  # output: <class 'str'>
print(type(emp))  # output: <class 'list'>

# create a variable info1 that stores a string : 'Jonathan' is an apple

print("He said: \\\"python\n's beauty is simplicity. \"")

# Converts input to float, then to int
x = int(float(input("Enter a number: ")))
y = float(input("Enter another number: "))
print(x, type(x))  # x is a string

print(x + y)  # This will concatenate the strings

str = 'Python'
version = 3
print(str + ' ' + str(3))  # output: Python 3

a = '1.5'
b = '2'

# Convert a to int, add b as int, then convert to float
c = float(float(a) + int(b))
print(c)  # output: 3.5

# using type casting create a variable called 'result' of a multiple by b that stores the result of the expression 1.5 + 2 store flot and will be 3.0
a = '1.5'
b = '2'
result = float(a) + float(b)  # Convert both a and b to float and add them
print(result)  # output: 3.5
# using type casting create a variable called 'result' of a multiple by b that stores the result of the expression 1.5 * 2 store float and will be 3.0
result = float(a) * float(b)  # Convert both a and b to float and multiply them
print(result)  # output: 3.0
