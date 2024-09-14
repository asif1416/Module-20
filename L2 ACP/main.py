# Tuple product
# Function to calculate product of elements in a tuple
def tuple_product(tup):
    product = 1
    for num in tup:
        product *= num  # Multiply each number with the running product
    return product

# Example tuples
tup1 = (4, 3, 2, 2, -1, 18)
tup2 = (2, 4, 8, 8, 3, 2, 9)

# Calculate and print the products
product1 = tuple_product(tup1)
product2 = tuple_product(tup2)

print(f"Product of elements in tup1: {product1}")
print(f"Product of elements in tup2: {product2}")
