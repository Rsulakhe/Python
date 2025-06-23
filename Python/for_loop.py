import math
import random

x = [12.21, 33, 2, 45, 22, 232, 12, 'Ri', 'Ro', 'Maddy']
1
for i in x:
    print(i)

for i in range(10):
    print(i)


for i in range(10, 20, 2):
    print(i)

for i in range(10, 0, -1):
    print(i)

for i in range(1, 500):
    if math.sqrt(i).is_integer():
        print(i)


for i in range(10):
    print(" ")
    for j in range(i):
        print("#", end="")


for i in range(10):
    print(" ")
    for j in range(j):
        print("#", end="")

for i in range(10):
    print(" ")
    for j in range(10):
        print("#", end="")

for i in range(10):

    print(" ")
    for j in range(10-i):
        print(j, end="")


my_str = input("Enter a string: ")
vowels = "aeiouAEIOU"
for item in my_str:
    if item in vowels:
        print(f"{item} is a vowel", end=" ")


c = 0
for i in 'abc xyz':
    c += 1
print(c)

for n in [1, 2, 4, 5, 6, 7, 8, 9, 10]:
    nn = n ** 2
    if nn % 2 == 0:
        print(f"{n} squared is {nn}, which is even.")
    else:
        print(f"{n} squared is {nn}, which is odd.")

r = range(1, 11)
print(r),
print(type(r))  # Output: <class 'range'>
print(list(r))  # Convert to list for better readability

print(list(range(1, 11)))  # Output: range(1, 11
print(list(range(1, 11, 2)))  # Output: 1
print(list(range(1, 100, 7)))

# Summary

# 1.range(stop)
print(list(range(10)))  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 2.range(start, stop)
print(list(range(5, 15)))  # Output: [5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

# 3.range(start, stop, step)
print(list(range(2, 20, 3)))  # Output: [2, 5, 8, 11, 14, 17]

# 4.range(start, stop, step) with negative step
print(list(range(10, 0, -2)))  # Output: [10, 8, 6, 4, 2]

# 5.range(start, stop, step) with negative step and start greater than stop
print(list(range(20, 10, -2)))  # Output: [20, 18, 16, 14, 12]

# Output: [-10, -7, -4, -1, 2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35, 38, 41, 44, 47, 50, 53, 56, 59, 62, 65, 68, 71, 74, 77, 80, 83, 86, 89, 92, 95, 98]
print(list(range(-10, 101, 3)))

print(sum(range(1, 1010)))  # Output: 505050

s = 0
for i in range(101):
    s += i
print(s)  # Output: 5050

for _ in range(10):
    print("Hello, World!", _)  # Output: Hello, World! (10 times)


names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Heidi", "Ivan", "Judy", "Kevin", "Leo",
         "Mallory", "Nina", "Oscar", "Peggy", "Quentin", "Rupert", "Sybil", "Trent", "Uma", "Victor", "Walter"]

for _ in range(4):
    print(f"Choosing winner for Round {_ + 1}")
    winner = random.choice(names)
    names.remove(winner)  # Remove the winner from the list to avoid repetitio
    print(f"Randomly selected name: {winner}")
    print("New Winner")

r = range(10)
print(r)  # Output: range(0, 10)

n = 10
for _ in range(5):
    print(n * 2)  # Output: 20 (5 times)

a, b, c, = 4, 5, 0

for i in range(5):
    c = a + b
print(c)

a = 5
if a < 5:
    for i in range(10):
        print(i, end=" ")
elif a > 5:
    for i in range(5):
        print(i, end=" ")
else:
    for i in range(3):
        print(i, end=" ")
