# List of comprehension practice
# Task 1: Generate a list of odd numbers below the input value
num = int(input("Enter a number: "))

# List comprehension to generate a list of odd numbers
odd_numbers = [i for i in range(num) if i % 2 != 0]

print("List of odd numbers below", num, ":", odd_numbers)

# Task 2: Convert first letter of fruits to uppercase
fruits = ['apple', 'banana', 'cherry', 'date']

# List comprehension to capitalize the first letter of each fruit
capitalized_fruits = [fruit.capitalize() for fruit in fruits]

print("List of fruits with capitalized first letter:", capitalized_fruits)

