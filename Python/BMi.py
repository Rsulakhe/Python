weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in centimeters: "))

# Convert height from cm to m for BMI calculation)
bmi = weight / height / height * 10000
print(bmi)

my_str = 'Python is TIOBE language of the year!'

# define veribale name s1 that stores the Character 'T' from the string above. Use a positive index to get the character.
s1 = my_str[10]  # 'T' is at index 10

# define veribale name s2 that stores the character 'r' from the string above. Use a negative index to get the character.
s2 = my_str[-6]  # 'r' is at index -6

print(my_str[:: -1])  # This will print the string in reverse order
# This will print every second character from index 0 to 10
print(my_str[0: 10:2])
print(my_str[10:])  # This will print the string from index 10 to the end
print(my_str[10:20])  # This will print the string from index 10 to 20

digits = '0123456789'

# This will slice the string from index -1 to -10 with a step of -3
x = digits[-1:: -3]
print(x)  # Output: '9753'

x = 2
y = 3
print(f'{x} - {y} = {x - y}')  # This will print:   # 2 - 3 = -1
# F-String also called as formatted string literals, allows you to embed expressions inside string literals, using curly braces `{}`.

# String Methods
my_str = 'Python is TIOBE language of the year!'
# This will print the list of all methods available for the string object
# upper case method
print(my_str.upper())

# lower case method
print(my_str.lower())

# count method
print(my_str.count('o'))  # Count occurrences of 'o'

# find method
print(my_str.find('TIOBE'))  # Find the index of 'TIOBE'

# replace method
print(my_str.replace('TIOBE', 'Python'))  # Replace 'TIOBE' with 'Python'

# split method
print(my_str.split())  # Split the string into a list of words

# join method
print(' '.join(['Python', 'is', 'fun']))  # Join a list of strings with spaces

# strip method
print(my_str.strip())  # Remove leading and trailing whitespace

print(':'.join('abcde'))  # Join characters with ':', output: 'a:b:c:d:e'

s = 'a-b-c-d-e-f-g'
print('-'.join(s.split('-')))  # Join with '-', output: 'a-b-c-d-e-f

# remove p from the string
my_str = 'Python is TIOBE language of the year!'
my_str = my_str.replace('P', '')  # Remove 'P' from the string
print(my_str)  # Output: 'ython is TIOBE language of the year!'


language = '$Python$$$',
massage = 'I love Python!'

language1 = print(language.replace('$', ''))
# string method to remove '$' from the string


language2 = print(language1.lower())  # Convert to lower case

massage1 = print(massage.replace('Python', 'Java')
                 )  # Replace 'Python' with 'Java'

massage2 = print(massage.upper())  # Convert to upper case

# python script to extract the address(00:0c:29:3e:4f:8bn) from the string
my_str = 'wL01 link encap : Ethernet  HWaddr 00:0c:29:3e:4f:8bn'
# Split the string and get the address part
address = my_str.split('HWaddr ')[1]
print(address)  # Output: '00:0c:29:3e:4f:8bn'
