# Function to encrypt the message
def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            # Shift within uppercase or lowercase letters
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char  # Non-alphabet characters are unchanged
    return result

# Function to decrypt the message
def decrypt(text, shift):
    return encrypt(text, -shift)

# Main Program
print("Simple Encryption/Decryption Tool (Caesar Cipher)")
choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").upper()
message = input("Enter your message: ")
shift = int(input("Enter shift value (e.g., 3): "))

if choice == 'E':
    encrypted = encrypt(message, shift)
    print("Encrypted message:", encrypted)
elif choice == 'D':
    decrypted = decrypt(message, shift)
    print("Decrypted message:", decrypted)
else:
    print("Invalid option.")
