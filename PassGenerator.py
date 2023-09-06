import random
import string

def generate_password(length):
    # Define the character set for the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Use random.choice to select random characters and join them to form the password
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def main():
    try:
        # Get the desired length of the password from the user
        length = int(input("Enter the desired password length: "))
        
        if length <= 0:
            print("Please enter a valid password length.")
            return

        # Generate the password
        password = generate_password(length)
        
        # Display the generated password
        print("Generated Password: " + password)
    
    except ValueError:
        print("Invalid input. Please enter a valid number for the password length.")

if __name__ == "__main__":
    main()
