
x = 8

r = x % 2
if r == 0:
    print("Even")
    if x > 7:
        print("Greater than 7")
    else:
        print("Less than 7")

print("Bye")

a = -12

if a < 0:
    print("Negative")
else:
    print("Positive")


a = input("Press Enter number : ")
b = input("Press Enter number : ")
c = input("Press Enter number : ")

a = int(a)
b = int(b)
c = int(c)

if a > b and a > c:
    print("a is greater")
elif b > a and b > c:
    print("b is greater")
elif c > a and c > b:
    print("c is greater")
else:
    print("All are equal")
