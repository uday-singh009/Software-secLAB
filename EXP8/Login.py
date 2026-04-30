import hashlib

# Take input
username = input("Enter username: ")
password = input("Enter password: ").encode()

found = False

# Read stored data
with open("users.txt", "r") as f:
    for line in f:
        stored_user, salt, stored_hash = line.strip().split(",")

        if stored_user == username:
            found = True
            salt = bytes.fromhex(salt)

            # Hash entered password with same salt
            new_hash = hashlib.sha256(salt + password).hexdigest()

            if new_hash == stored_hash:
                print("Login Successful ✅")
            else:
                print("Wrong Password ❌")

if not found:
    print("User not found ❌")
    
