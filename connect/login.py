import hashlib

pwd = 'secure password'
hashed = hashlib.sha256(pwd.encode()).hexdiget()
print("Stored hash:", hashed)

input_password = input("Enter password:")
input_hashed = hashlib.sha256(input_password.encode()).hexdigest()

if hashed == input_hashed:
    print("login success")
else:
    print("login failed")