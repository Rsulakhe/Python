# create a python script that asks user for number and then print out a list of all the divisors of each number less than the asked number

a = int(input("Give me a number"))
divisors = []
for n in range(1, a):
    if a % n == 0:
        divisors.append(n)
print(divisors)

# write python program to check if interger x is the power of another integer y. Prompt the user to input both integers

x = int(input("Enter the integer values of X: "))
y = int(input("Enter the integer value of y: "))

for n in range(2, x//2):
    if y ** n == x:
        print(f"{y} ** {n} = {x}")
else:
    print(f"{x} is not power of {y}")


# write a python program that counts and displays the vowels of a given string ignoring the letter case

my_str = "Hello EveryBody!"
vowels = "aeiouAEIOU"

count = 0
for v in vowels:
    if v in my_str.lower():
        count += my_str.count(v)
print(f"Total number of vowels: {count}")
