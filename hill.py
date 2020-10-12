def hill_encryption(message, key):
    encrypted_message = ''
    for letter in range(message):
        if letter == ' ':
            encrypted_message = encrypted_message + letter
        else:
            encrypted_message = encrypted_message + letter