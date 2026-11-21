
i = 1
while i <= 5:
    print("This is a while loop", end="")
    j = 1
    while j <= 5:
        print(" Starting inner loop", j, end="")
        j += 1
    i += 1
    print(".")


# write code to print the all the values from 1 to 100 skip the numbers which are divisible by 3 and 5

a = 1
while a <= 100:
    if a % 3 != 0 and a % 5 != 0:
        print(a, end=" ")
    a += 1

# print the # in line and the number of # in each line is equal to the line number


x = 1
while x <= 5:
    y = 1
    while y <= 5:
        print("#", end="")
        y += 1
    print()
    x += 1
