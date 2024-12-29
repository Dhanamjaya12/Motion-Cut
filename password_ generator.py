import random
import string

# Function to generate a random password
def generate_password(length):
    # Define the character categories
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation

    # Password contains at least one character from each category
    all_characters = uppercase_letters + lowercase_letters + digits + special_characters

    # Randomly select one character 
    password = [
        random.choice(uppercase_letters),
        random.choice(lowercase_letters),
        random.choice(digits),
        random.choice(special_characters)
    ]
    
    #  Password length with random characters from all categories
    password += random.choices(all_characters, k=length - 4)
    
    # Shuffle the password 
    random.shuffle(password)
    
    # Join the password list into a string and return it
    return ''.join(password)

# Function to get user input and validate the password length
def main():
    print("Welcome to the Random Password Generator!")
    
    # Get the desired password length from the user
    while True:
        try:
            length = int(input("Enter the desired password length (minimum 8): "))
            if length < 8:
                print("Password length must be at least 8 characters.")
            else:
                break
        except ValueError:
            print("Invalid input! Please enter a number.")
    
    # Generate and display the password
    password = generate_password(length)
    print(f"Your randomly generated password is: {password}")

# Run the program
if __name__ == "__main__":
    main()