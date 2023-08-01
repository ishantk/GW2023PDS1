# Encrypting Data
import hashlib
password = input("Enter the Password: ")
# Encode Password to UTF-8
password = password.encode('utf-8')
# Generate the Secure SHA 256 Hash
password = hashlib.sha256(password).hexdigest()
print(password)