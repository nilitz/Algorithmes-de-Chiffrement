import math

import numpy as np


def prime_numbers(max):
    array = []
    count = 3

    while count < max:
        is_prime = True

        for x in range(2, int(math.sqrt(count) + 1)):
            if count % x == 0:
                is_prime = False
                break

        if is_prime:
            array.insert(len(array), count)

        count += 1
    return array


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
    determinant = int(np.linalg.det(key))
    inverse = np.linalg.inv(key) * determinant
    decryption_matrix = key

    prime_array = prime_numbers(500)
    i = 0
    tested_prime = prime_array[i]

    while (determinant * tested_prime) % 26 != 1:
        i = i + 1
        tested_prime = prime_array[i]

    for l in range(0, len(inverse)):
        for c in range(0, len(inverse[0])):
            decryption_matrix[l][c] = int(round(inverse[l][c]))
    matrix = (tested_prime * decryption_matrix) % 26

    return matrix_calcul(encrypted_message, matrix)
