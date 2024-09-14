# Check the frequency
# Test dictionary
test_dict = {'Codingal': 3, 'is': 2, 'best': 2, 'for': 2, 'Coding': 1}

# Print the dictionary
print("Test dictionary:", test_dict)

# Ask the user to enter a value to check its frequency
value = int(input("Enter the value to check its frequency: "))

# Count the frequency of the value
frequency = list(test_dict.values()).count(value)

# Print the result
print(f"The frequency of value {value} in the dictionary is: {frequency}")

