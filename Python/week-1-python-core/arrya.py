
from array import array


a = array('i', [1, 2, 3, 4, 5])

print(type(a))

b = array('d', [2.5, 3.8, -3.2, 4.8, 5.0])

print(type(b))

# iterating through the array using for loop
for value in b:
    # condition to skip negative values
    if value < 0:
        continue
    print(value)
