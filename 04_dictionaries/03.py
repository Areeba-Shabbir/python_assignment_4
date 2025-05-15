import hashlib

# Function to hash a password using SHA256
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Function to check if the given email and password match
def login(email, password_to_check, stored_logins):
    # Hash the password provided for login
    hashed_password = hash_password(password_to_check)
    
    # Compare it with the stored hashed password
    if email in stored_logins and stored_logins[email] == hashed_password:
        return True
    else:
        return False

def main():
    # Stored logins: emails with hashed passwords
    stored_logins = {
        "user1@example.com": hash_password("secure123"),
        "user2@example.com": hash_password("myPassword"),
        "user3@example.com": hash_password("abc123")
    }

    # Ask for email and password
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    # Check login
    if login(email, password, stored_logins):
        print("Login successful!")
    else:
        print("Login failed! Check your email or password.")

if __name__ == '__main__':
    main()
