import base64 as b64
import hashlib
import string


def encryption(message):
    m = hashlib.md5()
    m.update(message.encode('utf-8'))
    return m.hexdigest()


def message_alternative(message):
    message_array = [message.lower()]
    message_array.insert(len(message_array), message.upper())
    message_array.insert(len(message_array), message + '*')
    for letter in string.ascii_letters:
        message_array.insert(len(message_array), letter + message)
        message_array.insert(len(message_array), letter + message + '*')
        message_array.insert(len(message_array), message + letter)
        for number in range(1950, 2021):
            message_array.insert(len(message_array), letter + message + number.__str__())
            message_array.insert(len(message_array), message + number.__str__())
            message_array.insert(len(message_array), message + number.__str__() + '*')
    return message_array


def browse_file(name, searched_md5):
    file = open("./resources/dictionaries/" + name)
    i = 1
    for line in file:
        line_message = line.replace("\n", '')
        line_message_array = message_alternative(line_message)
        for message in line_message_array:
            line_encrypted = encryption(message)
            i = i + 1

            if line_encrypted == searched_md5:
                print(
                    "--------------------------------------------"
                    "\nThe tested word is : ",
                    message,
                    "\nThe tested word md5 is : ",
                    line_encrypted,
                    "\nThe searched md5 is :",
                    searched_md5
                )
                print(
                    "FOUND",
                    "\n--------------------------------------------"
                )
                break
    print("iteration : ", i)


def decryption(md5):
    browse_file("multi-langues-mot-de-passe-par-defaut.txt", md5)
    browse_file("francais-prenoms.txt", md5)
    browse_file("francais-divers.txt", md5)
