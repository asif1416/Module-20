# Square it out
def square_and_filter_odd_even(start, end):
    squares = [i**2 for i in range(start, end + 1)]
    
    # Filter odd and even square values
    odd_squares = [sq for sq in squares if sq % 2 != 0]
    even_squares = [sq for sq in squares if sq % 2 == 0]
    
    # Print the results
    print("Odd squares:", odd_squares)
    print("Even squares:", even_squares)

# Example usage
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
square_and_filter_odd_even(start, end)
