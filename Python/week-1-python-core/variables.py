import math

x = 9
y = 10

x + y
_ = x + y
# Define _ explicitly
_ + y
# 19 _ is now explicitly defined
x + _
# 19 _ is a placeholder for the last expression in the interpreter


# Strings in python are immutable, meaning they cannot be changed after creation.

# However, you can create a new string based on the original string with modifications.


studendtCount = 1000
print(studendtCount)
rating = 4.99
is_published = True
course_name = "Python Programming"

len(course_name)
print(len(course_name))
print(course_name[0: 7])
print(course_name[0:])
print(course_name[: 10])

course_name = "Python Programming"
print(course_name.upper())
print(course_name.lower())
print(course_name.title())
print(course_name.find("m"))
print(course_name.replace("m", "J"))
print("pro" in course_name)
print("Pro" not in course_name)
print("Python" in course_name)

print(round(2.9))
print(abs(-2.9))
print(math.ceil(2.1))

fruit = "Apple"
print(fruit[1: -1])
