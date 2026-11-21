
# Display the following strings literally:

import random
print('It Displayed : "You\'ve got an email"')
print('"\n means a new line')
print('"\ is known as an escape character')

# write python script that converts foot to centimeters 1ft = 30.48cm

foot_val = float(input("Enter the value in feet: "))
cenitmeters_val = foot_val * 30.48
print(f"{foot_val} feet is equal to {cenitmeters_val} centimeters.")

# write python script that test if a string is a palindrome or not

s = input("Enter a string to check if it's a palindrome: ")
s1 = s.lower().replace(" ", "")  # Normalize the string
s2 = s1[::-1]  # Reverse the string
if s1 == s2:
    print(f"{s} is a palindrome.")
else:
    print(f"{s} is not a palindrome.")

# write python script to get string made of the first and last 2 character of a given string

first = input("Enter a string: ")

# Ticket booking system

Balance = 1000  # Initial balance
price = float(input("Enter the ticket price: "))
if price < Balance:
    Balance = Balance - price
    print(f"Ticket booked successfully! Remaining balance: {Balance}")
else:
    print("Insufficient balance to book the ticket.")


a = -1
if a:
    print("a is True")
else:
    print("a is False")

animals = ["cat", "dog", "elephant", "fish", "tiger", "lion"]
choice = random.choice(animals)

if choice == "cat":
    print("Hi Tom it's your turn to play")
elif choice == "dog":

    print("Hi Scubby it's your turn to play")
elif choice == "elephant":
    print("Hi Dumbo it's your turn to play")
elif choice == "tiger":
    print("Hi Sher Khan it's your turn to play")
elif choice == "lion":
    print("Hi Simba it's your turn to play")
elif choice == "fish":
    print("Hi Nemo it's your turn to play")
else:

    print("No animal selected, please try again.")

for lettier in "Python":
    print(lettier)
