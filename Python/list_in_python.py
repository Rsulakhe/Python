nums = [25, 12, 50, 89, 75, 88, 100]
print(nums[0])  # Output: 25

names = ["John", "Jane", "Doe"]
print(names[1])  # Output: Jane

# Add multiple elements to the end of the list
nums.extend([11, 12, 44, 555, 12, 55, 6, 5])
nums
del nums[5:]  # Delete elements from the list starting from index 5 to the end
nums

# Tuple is immutable, meaning it cannot be changed after creation. ittration in tuple is faster than list.


tup = (1, 2, 3, 4, 5)
print(tup[0])  # Output: 1
print(tup[1])  # Output: 2
print(tup[2])  # Output: 3


keys = ["rohit", "sachin", "saurav"]
values = [1, 2, 3]

porgs = {'js': {'JSE': 'Netbeans', 'jee': 'Eclipse'}, 'java': 'Eclipse',
         'python': ['PyCharm', 'subline, jupiter'], 'CSS': 'VSCode'}
