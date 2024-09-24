def caesar_cipher(text, shift, direction):
    result = ""
    shift = shift % 26  # Ensure the shift value is within the range of the alphabet
    
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            shift_amount = shift if direction == "encrypt" else -shift
            char_code = ord(char)
            offset = 65 if char.isupper() else 97
            new_char = chr(((char_code - offset + shift_amount) % 26) + offset)
            result += new_char
        else:
            result += char  # Non-alphabet characters remain unchanged

    return result

# Get user input
text = input("Enter your message: ")
shift = int(input("Enter the shift value: "))
direction = input("Type 'encrypt' to encrypt or 'decrypt' to decrypt: ").lower()

# Perform encryption or decryption
result = caesar_cipher(text, shift, direction)
print(f"The {direction}ed message is: {result}")