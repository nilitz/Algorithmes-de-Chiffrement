def number_to_letter(number):
    if number < 65:
        letter = chr(90 - (65 - number))
    else:
        letter = chr(number)
    return letter


def translation(message, key):
    message = message.upper()
    new_message = ''
    for letter in message:
        if letter == ' ':
            new_message = new_message + letter
        else:
            letter = number_to_letter(ord(letter) - key)
            new_message = new_message + letter
    return new_message


def encryption(message, key):
    print(
        "- - - - - C E S A R - E N C R Y P T I O N - - - - -\n",
        "The result with the reducer ", key, " is : ",
        translation(message, key),
        "\n- - - - - E N D - - - - -\n"
    )


def decryption(message):
    print("- - - - - B R U T - F O R C E - C E S A R - - - - -")
    for key in range(1, 25):
        print(
            "The result with the reducer ",
            key, " is : ",
            translation(message, key)
        )
    print(" - - - - - E N D - - - - -\n")