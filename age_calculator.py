from datetime import datetime

name = input("Enter your name: ")

try:
    age = int(input("Enter your age: "))
    num = int(input("How many times you wanna print the message: "))
except ValueError:
    print("Please enter valid numbers for age and repetitions.")
    exit()

if age < 0:
    print("Age cannot be negative.")
    exit()

if num <= 0:
    print("The number of repetitions must be greater than zero.")
    exit()

current_year = datetime.now().year
your_turn_100 = current_year + (100 - age)

message = (f"{name},If you are {age} years old in {current_year},then you will be 100 years old in {your_turn_100}")

for _ in range(num):
    print(message)

