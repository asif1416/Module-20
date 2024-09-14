# Set and Arrays
# Function to find symmetric difference
def find_symmetric_difference(set1, set2):
    return set1.symmetric_difference(set2)

# Example A: Symmetric difference between two sets of colors
set1_A = {'blue', 'green'}
set2_A = {'blue', 'yellow'}
symmetric_diff_A = find_symmetric_difference(set1_A, set2_A)

# Example B: Symmetric difference between two sets of numbers
set1_B = {1, 2, 3, 4, 5}
set2_B = {1, 5, 6, 7, 8, 9}
symmetric_diff_B = find_symmetric_difference(set1_B, set2_B)

# Print the results
print(f"Symmetric difference (A) between {set1_A} and {set2_A} is: {symmetric_diff_A}")
print(f"Symmetric difference (B) between {set1_B} and {set2_B} is: {symmetric_diff_B}")
