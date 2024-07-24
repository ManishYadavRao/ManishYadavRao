def encrypt(text, shift):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def get_shift():
    while True:
        try:
            shift = int(input("Enter shift value: "))
            return shift
        except ValueError:
            print("Invalid input. Please enter an integer.")

def main():
    while True:
        print("\nCaesar Cipher Program")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            text = input("Enter your message: ")
            shift = get_shift()
            print("Encrypted message: " + encrypt(text, shift))
        elif choice == '2':
            text = input("Enter your message: ")
            shift = get_shift()
            print("Decrypted message: " + decrypt(text, shift))
        elif choice == '3':
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()
