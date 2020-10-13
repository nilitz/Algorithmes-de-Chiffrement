import cesar
import md5
import hill_responsive
import numpy as np
import math

if __name__ == '__main__':
    # HILL DEMONSTRATION :

    print("-------------- HILL --------------")
    hill_decrypted_message = 'jevouse'
    print("message : ", hill_decrypted_message)

    hill_encryption_matrix = np.array([[9, 4], [5, 7]])
    hill_encrypted_message = hill_responsive.hill_responsive_encryption(hill_decrypted_message, hill_encryption_matrix)
    hill_decrypted_message = hill_responsive.hill_responsive_decryption(hill_encrypted_message,np.array([[9, 4], [5, 7]]))
    print("used matrix :\n", hill_encryption_matrix, "\nencrypted message : ", hill_encrypted_message, "\ndecrypted message : ", hill_decrypted_message, "\n-------------- BREAK --------------")

    hill_encryption_matrix = np.array([[1, 3, -1], [6, 1, 1], [-5, 4, -3]])
    hill_encrypted_message = hill_responsive.hill_responsive_encryption(hill_decrypted_message, hill_encryption_matrix)
    hill_decrypted_message = hill_responsive.hill_responsive_decryption(hill_encrypted_message, hill_encryption_matrix)

    print("used matrix :\n", hill_encryption_matrix, "\nencrypted message : ", hill_encrypted_message, "\ndecrypted message : ", hill_decrypted_message, "\n-------------- BREAK --------------")

    """
    # MD5 DEMONSTRATION :

    md5_encrypted_message = '6d1523b39a9904958cada602dc52c7d4'
    md5.encryption('hello')  # hello
    md5.decryption(md5_encrypted_message)
    """

    """
    # CESAR DEMONSTRATION :
    
    cesar_encrypted_message = 'oh kdfkdjh yrxv shuphwwudlw gdvvxuhu od frqilghqwldolwh vlpsohphqw'
    cesar.decryption(cesar_encrypted_message)

    cesar_decrypted_message = 'LE HACHAGE VOUS PERMETTRAIT DASSURER LA CONFIDENTIALITE SIMPLEMENT'
    cesar.encryption(cesar_decrypted_message, 22)
    """
