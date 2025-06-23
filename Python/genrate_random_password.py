
import random
import string

charactors = string.ascii_letters + string.digits + string.punctuation

# Generate a random password of specified length
pass_length = int((input("Enter the length of the password: ")))
password = ""

for i in range(pass_length):
    c = random.choice(charactors)
    password += c

print("Generated password:", password)  # Print the generated password


# for, cotinue, break, pass statements

for letter in "Go python Gooooo !!":
    if letter == "o":
        continue  # Skip the letter 'o'
    print(letter, end=" ")

for i in range(100):
    if i % 2 == 0:
        print(f"{i} is even")
        continue
    print(f"{i} is odd")  # This will only print for odd numbers

for letter in "pythoooon !!!":
    if letter == "o":
        continue  # Skip the letter 'o
    print(letter, end=" ")  # output: pythn !!!

for i in range(5):
    if i == 1:
        pass
    # This will print all numbers from 0 to 4, including 1
    print(f"Current number is {i}")

nums = [1, 2, 4, 7, 8]
s = 0
for n in nums:
    s += n
    if s >= 4:
        break  # Exit the loop when the sum is greater than or equal to 4
print(f"s ={s}")  # Output: Sum is 7, since it breaks when the sum reaches 4

for x in range(7):
    if (x == 3 or x == 6):
        continue  # Skip the numbers 3 and 6
    print(x, end="#")  # Output: 0#1#2#4#5#

for i in range(18, -4, 5):
    if i == 13:
        continue  # Skip the number 13
    print(i, end=" ")  # Output: 18 8 3 -2

for i in range(10):
    print(i, end=" ")
    if i == 5:
        break
    else:
        print("Continuing the loop")  # This will print for numbers less than 5
print("\n after the loop ends")  # This will print after the loop ends

# using for loop and the range function the sum and the product of numbers between 1 and 25 (both included)
my_sum = 0
my_product = 1
for i in range(1, 26):
    my_sum += i  # Add the current number to the sum
    my_product *= i  # Multiply the current number to the product
# Output: Sum of numbers from 1 to 25 is: 325
print(f"Sum of numbers from 1 to 25 is: {my_sum}")
# Output: Product of numbers from 1 to 25 is: 15511210043330985984000000
print(f"Product of numbers from 1 to 25 is: {my_product}")


while True:
    a = 1
    if a:
        break  # This will break the loop immediately
    print(a)  # This line will never be executed because the loop breaks immediately

for letter in "word":
    i = 3
    while i > 0:
        i -= 1  # Decrement i by 1
        print(letter, end=" ")  # Print the letter
    print('')  # Print a newline after each letter

a = 5
while a < 7:
    a += 5
    print(a)

x = 5
while x > 0:
    x -= 1
else:
    print('Bye !')

while True:
    a = 1
    if a:
        break
    print(a)

while True:
    a = 1
    print(a)
    a += 2
    if a > 2:
        break

for letter in 'Wood':
    i = 3
    while i > 0:
        i -= 1
        print(letter, end='')
    print(' ')

a = 10
while a > 0:
    a -= 1
    if a % 2 == 0:
        continue
    print(a, end='')


x = 5
s = 0
while x:
    x -= 1
    s += x
print(s)

x = 5
while x > 5:
    x -= 1
    if x == 1:
        break
else:
    print('Bye !')

a = 1
my_sum = 0
while a < 100:
    if a % 2 != 0:
        my_sum += a
    a += 1
print(f"Sum of all the odd numbers between 1 to 100 is: {my_sum}")

while (x := input("Enter something here")) != '':
    print(x)
