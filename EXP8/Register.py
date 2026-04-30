import hashlib
import os

# Take input
username = input("Enter username: ")
password = input("Enter password: ").encode()

# Generate random salt
salt = os.urandom(16)

# Create hash (salt + password)
hashed_password = hashlib.sha256(salt + password).hexdigest()

# Store in file
with open("users.txt", "a") as f:
    f.write(f"{username},{salt.hex()},{hashed_password}\n")

print("User registered successfully!")
