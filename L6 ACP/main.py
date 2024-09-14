# Random Password Generator
import random

# Function to generate a random password
def generate_password(length):
    if length < 6:  # Minimum password length check
        return "Password length should be at least 6 characters."
    
    # Define base character pool
    letters = 'abcdefghijklmnopqrstuvwxyz'
    digits = '0123456789'
    
    # Use .lower() and .upper() to create character pools
    lower = letters.lower()    # This gives us lower case letters
    upper = letters.upper()    # This gives us upper case
    
    # Ensuring password contains at least one lowercase, one uppercase, and one digit
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits)
    ]
    
    # Filling the rest of the password with random choices from all character pools
    all_characters = lower + upper + digits
    password += random.choices(all_characters, k=length - 3)
    
    # Shuffle the generated password to ensure randomness
    random.shuffle(password)
    
    # Convert list to string and return
    return ''.join(password)

# Example usage
length = int(input("Enter the desired password length (minimum 6): "))
password = generate_password(length)
print("Generated password:", password)
