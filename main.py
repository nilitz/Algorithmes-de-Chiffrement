import cesar
import md5
import hill_responsive
import numpy as np
import math


def hill(hill_decrypted_message, hill_encryption_matrix):
    print(
        "used matrix :\n", hill_encryption_matrix
    )
    hill_encrypted_message = hill_responsive.hill_responsive_encryption(hill_decrypted_message, hill_encryption_matrix)
    hill_decrypted_message = hill_responsive.hill_responsive_decryption(hill_encrypted_message, hill_encryption_matrix)
    print(
        "encrypted message : ", hill_encrypted_message,
        "\ndecrypted message : ", hill_decrypted_message,
    )


if __name__ == '__main__':
    # HILL DEMONSTRATION :

    hill('jevousaime', np.array([[9, 4], [5, 7]]))
    hill('dictionnaire', np.array([[1, 3, -1], [6, 1, 1], [-5, 4, -3]]))

    """
    # MD5 DEMONSTRATION :

    md5.encryption('hello')  # hello
    md5.decryption('6d1523b39a9904958cada602dc52c7d4')
    


    # CESAR DEMONSTRATION :
    

    cesar.decryption('oh kdfkdjh yrxv shuphwwudlw gdvvxuhu od frqilghqwldolwh vlpsohphqw')

    cesar.encryption('LE HACHAGE VOUS PERMETTRAIT DASSURER LA CONFIDENTIALITE SIMPLEMENT', 22)
"""
