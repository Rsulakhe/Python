
li = [1, 2, 4, 5, 'python', True, ['abc', 'xyz'], (10, 20, 30)]
print(len(li))
l2 = []  # Empty list
l3 = list()  # empty list

x = li[-1]
print(x)

l4 = list('abcde')
print(id(l4))
print(l4)
l4[0] = 'Tiwtter'
l4.append(200)
print(l4)

# extend
l4.extend([11, 12])
print(l4)
l4.append([99, 45, 12, 45])
print(l4)

# reptarion

l5 = list('abced')
l6 = l5 * 3
print(l6)

# List Slicing
# slicing Modifies the list

Numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
nums = Numbers[1:5]
print(f'print nums {nums}')
print(f'print Numbers {Numbers}')
print(Numbers[:3])  # start is default zero
print(Numbers[2:])  # stop is default the end of the list
print(Numbers[1:5:3])  # print the list in the gap of 3
print(Numbers[::])  # print the entier list
print(Numbers[:: -1])  # Will print the list in reverse order

Numbers[0:2] = ['a', 'b', 'c']


# Python List Gotchas

l1 = [1, 2, 3]
l2 = l1
l2[0] = 'XX'
l2.append(12)
print(f"l2 : {l2}")
print(f"l1 : {l1}")

#
nums1 = [1, 2, 3, 4, 5, 6, 78, 9, 20]

# this is wrong!
for n in nums1:
    if n < 5:
        nums1.remove(n)
print(nums1)

# Right way to do it
new_list = []
for n in nums1:
    if n >= 5:
        new_list.append(n)
print(new_list)

# another way finding the greater numbers in list
my_list = [n for n in nums1
           if n >= 5]
print(my_list)

l1 = list('ab')
l2 = l1
l1 = []
print(l2)

my_list1 = [2.45, 12, 'Roni', [12, 131, 10]]
x = my_list1[1]
print(x)
y = my_list1[1:][-1][1]
print(y)
