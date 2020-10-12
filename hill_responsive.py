import math

import numpy as np


def matrix_calcul(message, key):
    message = message.upper()

    analysed_message = ''

    for i in range(0, len(message), len(key)):
        temporary_array = []

        for j in range(i, i + len(key)):
            if j >= len(message):
                temporary_array.append(0)
            else:
                temporary_array.insert(len(temporary_array), ord(message[j]) - 64)
        for l in range(0, len(key)):
            tempo = 0
            for c in range(0, len(key[0])):
                if temporary_array[c] == 0:
                    tempo = tempo + (-key[l][c])
                else:
                    tempo = tempo + (key[l][c] * temporary_array[c])
            tempo = tempo % 26

            if tempo == 0:
                tempo = 26
            analysed_message = analysed_message + chr(tempo + 64)

    return analysed_message


def hill_responsive_encryption(message, key):

    encrypted_message = matrix_calcul(message, key)
    return encrypted_message


def hill_responsive_decryption(encrypted_message, key):

    inversed_key = np.linalg.inv(key)
    print(inversed_key)
