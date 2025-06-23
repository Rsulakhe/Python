li = list()

print(li)

# append list.append()
li.append(5)
# li.append(6, 7) # Error
li.append([6, 5, 7])
print(li)

# Extend list.extend
li.extend('xy')
print(li)

# Insert list.insert()
years = [2020, 2022, 2024]
years.insert(1, 2021)
years.insert(len(years), 2025)
print(years)

# Clear list.clear()
years.clear()
print(years)

# pop list.pop() it removes from given index and returns the removed element
l2 = [12, 10, 1, 12, 10, 12, 88, 11, 43, 12, 12, 22, 53]
x = l2.pop()
print(x)
print(l2)

# Remove list.remove()
l2.remove(12)
print(l2)

while 12 in l2:
    l2.remove(12)
print(l2)

# Index of the specific element list.index()
names = ['Jon', 'ron', 'bill', 'Surya', 'Rolex']
i = names.index('Rolex')
print(i)

# Count list.count() it retuns count of perticaluar element in a list
letter = list(
    'aferadfadklfjhadfaosdifadosfhasdlkfashdgfasdhfuasofaudhfasdhfasdfhsdanflasdfadsgf9tghfsdaz')
n = letter.count('a')
print(n)
print('b' in letter)

# reverse list.reverse() it reverse the order of element in the list

l2.reverse()
print(f'the list after reverse: {l2}')

# sort list.sort() and sorted list(list)
l3 = [12, 21, 44, 11, 5, 99, 7, 19, 55, 12, 55, 121, 221, 556, 9]
la = sorted(l3)
print(la, l3)

n = l3.sort()
print(n)
print(l3)
l3.sort(reverse=True)
print(l3)

# Max() and min()

print(max(l3))
print(min(l3))
print(sum(l3))

# convert list to the stirng using split() and join() methods used to convert list to string

mysTr = 'I am learning python programming'
newStr = mysTr.split()
print(newStr)

name_list = ['Alice', 'Bob', 'Eve']
url = 'www.python.org'

name_str = '.'.join(name_list)
print(name_str)

url_list = url.split('.')
print(url_list)

nums = [1, 4, 1, 10, 2.4, 5.5]
sorted(nums, reverse=True)
print(nums)
print(nums.index(1))

nums.extend([len(nums), max(nums)])

print(nums)

names = ['Dan', 'Mario', 'Andu']
names.insert(2, 'Hanna')
print(names)

# list Comperhesion
# List comprehension offers us a shorter and more concise syntax to create a new list bases on the values of an exisiting iterable

click_sequal = [3, 1, 5, 6, 1, 4, 66, 12]
doubled_list = list()
doubled_list = [c * 2 for c in click_sequal]
print(doubled_list)


friends = ['Jon', 'Hani', 'Marry', 'luna']
neighbors = ['Tim', 'Steve', 'Dan', 'Hani', 'Marry'
             '', 'Jon']
friends_and_neighbors = [name for name in friends if name in neighbors]
print(friends_and_neighbors)

names1 = ['Dan', 'Mario', 'Andu']
l = [len(n) for n in names1 if 'a' in n]
print(l)
