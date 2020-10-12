import math

import numpy as np


def matrix_calcul(message, key):
    message = message.upper()

    analysed_message = ''

    for i in range(0, len(message), len(key)):
        temporary_array = []
        temporary_array.insert(len(temporary_array), ord(message[i]) - 64)

        for j in range(i, i + len(key)):
            if j >= len(message):
                temporary_array.append(0)
            else:
                temporary_array.insert(len(temporary_array), ord(message[i + 1]) - 64)
        for l in range(0, len(key)):
            tempo = 0
            for c in range(0, len(key[0])):
                tempo = tempo + (key[l][c] * temporary_array[c])
            tempo = tempo % 26
            analysed_message = analysed_message + chr(tempo + 64)
            print(analysed_message)

    return analysed_message


def hill_responsive_encryption(message, key):
    encrypted_message = matrix_calcul(message, key)
    return encrypted_message
