a = 5
b = 7

# Swap two numbers without using a third variable
a = a + b
b = a - b
a = a - b

print("After swapping:")
print("a =", a)
print("b =", b)

# Swap two numbers using a third variable
a = 5
b = 7

temp = a
a = b
b = temp

print("After swapping with a third variable:")
print("a =", a)
print("b =", b)

a = 9
b = 8

a, b = b, a
# rotate the values of a and b
print("After swapping with a third variable:")
print("a =", a)
print("b =", b)

a = a ^ b
b = a ^ b
a = a ^ b

print("After swapping with a third variable:")
print("a =", a)
print("b =", b)
