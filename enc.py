def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char 
    return result
def decrypt(text, shift):
    return encrypt(text, -shift)
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
