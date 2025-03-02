from cryptography.fernet import Fernet

def generate_key():
    """Generates a 128-bit AES key."""
    key = Fernet.generate_key()
    return key

def encrypt_message(message, key):
    """Encrypts a message using AES-128."""
    f = Fernet(key)
    encrypted_message = f.encrypt(message.encode())
    return encrypted_message.decode()

def decrypt_message(encrypted_message, key):
    """Decrypts an encrypted message using AES-128."""
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message.encode()).decode()
    return decrypted_message

# Generate a key
key = generate_key()

# Get the message from the user
message = input("Enter your message: ")

# Encrypt the message
encrypted_message = encrypt_message(message, key)

# Print the encrypted message
print("Encrypted message:", encrypted_message)

# Add the decrypter functionality:
encrypted_input = input("Enter the encrypted message: ")
decrypted_message = decrypt_message(encrypted_input, key)
print("Decrypted message:", decrypted_message)

