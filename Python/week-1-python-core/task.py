
x = int(input("Enter a number of candies you want: "))
candiesAvailable = 10

i = 1
while i <= x:
    if i > candiesAvailable:
        print("Sorry, I don't have that many candies")
        break
    print("i have", i, "candies")
    i += 1
print("I don't have any more candies")


# print to all the values except the values are devisible by 3 and 5

for i in range(1, 101):
    if i % 3 == 0:
        continue
    print(i)


# print to all the values except the values are devisible by 3 and 5
for i in range(1, 101):
    if i % 3 == 0 or i % 5 == 0:
        continue
    print(i)
