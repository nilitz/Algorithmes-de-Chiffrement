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
    for i in range(0, len(message), 2):
        temporary_x = ord(message[i]) - 64
        if i + 1 >= len(message):
            temporary_y = 0
        else:
            temporary_y = ord(message[i + 1]) - 64

        encrypted_temporary_x = (key[0][0] * temporary_x + key[0][1] * temporary_y) % 26
        encrypted_temporary_y = (key[1][0] * temporary_x + key[1][1] * temporary_y) % 26
        analysed_message = analysed_message + chr(encrypted_temporary_x + 64) + chr(encrypted_temporary_y + 64)
    return analysed_message


def hill_encryption(message, key):
    encrypted_message = matrix_calcul(message, key)
    return encrypted_message

def get_inverse(matrix):
    for l in range(0, len(matrix)):
        for c in range(0, len(matrix[0])):
            print('test')


def hill_decryption(encrypted_message, key):
    encrypted_message = encrypted_message.upper()

    multiplier = (key[0][0] * key[1][1] - key[0][1] * key[1][0])
    matrix = np.array([[key[1][1], - key[0][1]], [- key[1][0], key[0][0]]])

    prime_array = prime_numbers(multiplier)

    print(get_inverse(key))
    inversed_key = np.linalg.inv(key)

    print(inversed_key)

    i = 0
    tested_prime = prime_array[i]

    while (multiplier * tested_prime) % 26 != 1:
        i = i + 1
        tested_prime = prime_array[i]

    matrix = (tested_prime * matrix) % 26

    decrypted_message = matrix_calcul(encrypted_message, matrix)

    return decrypted_message
