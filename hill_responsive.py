import math

import numpy as np


def matrix_calculus(message, key):
    message = message.upper()

    analysed_message = ''

    for i in range(0, len(message), len(key)):
        temporary_array = []

        for j in range(i, i + len(key)):
            if j >= len(message):
                temporary_array.append(0)
            else:
                temporary_array.insert(len(temporary_array), ord(message[j]) - 64)
        for r in range(0, len(key)):
            tempo = 0
            for c in range(0, len(key[0])):
                if temporary_array[c] == 0:
                    tempo = tempo + (-key[r][c])
                else:
                    tempo = tempo + (key[r][c] * temporary_array[c])
            tempo = tempo % 26

            if tempo == 0:
                tempo = 26
            analysed_message = analysed_message + chr(tempo + 64)

    return analysed_message


def hill_responsive_encryption(message, key):
    encrypted_message = matrix_calculus(message, key)
    return encrypted_message


def hill_responsive_decryption(encrypted_message, key):
    determinant = int(np.linalg.det(key))
    inverse = np.linalg.inv(key) * determinant
    decryption_matrix = key

    i = 0

    array = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]

    new_tested_prime = array[i]

    while (determinant * new_tested_prime) % 26 != 1:
        i = i + 1
        new_tested_prime = array[i]

    for r in range(0, len(inverse)):
        for c in range(0, len(inverse[0])):
            decryption_matrix[r][c] = int(round(inverse[r][c]))
    matrix = (new_tested_prime * decryption_matrix) % 26

    return matrix_calculus(encrypted_message, matrix)