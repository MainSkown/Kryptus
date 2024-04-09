import numpy as np
import math


def encrypt(text: str, key: str) -> str:
    if len(key) != 11:
        raise ValueError('Key must be 11 characters long')
    # Encrypted text
    encrypted_text = ""

    # Create a 3x3 matrix from 9 ASCII values of characters of the key
    key_matrix = np.array([ord(key[i]) for i in range(9)]).reshape(3, 3)

    # Modulo value - 2 char values of keys added together
    modulo_value = ord(key[9]) + ord(key[10])

    for char in text:
        # Convert character to ASCII value
        char_value = ord(char)

        # Create copy of key_matrix
        key_matrix_copy = key_matrix.copy()

        # Multiply copy by char_value
        key_matrix_copy = key_matrix_copy * char_value
        # Transpose copy
        key_matrix_copy = key_matrix_copy.T

        simplify = np.multiply(key_matrix_copy, np.array([[1], [1], [1]]))

        sum_of_division = 0
        for i in range(3):
            encrypted_text += chr(simplify[i][0] % modulo_value)
            sum_of_division += math.floor(simplify[i][0] / modulo_value)
        encrypted_text += chr(sum_of_division)

    return encrypted_text


def decrypt(text: str, key: str) -> str:
    # split text in to list of 4
    text = [text[i:i + 4] for i in range(0, len(text), 4)]
    decrypted_text = ""

    # Create a 3x3 matrix from 9 ASCII values of characters of the key
    key_matrix = np.array([ord(key[i]) for i in range(9)]).reshape(3, 3)
    key_matrix = key_matrix.T
    simplify = np.multiply(key_matrix, np.array([[1], [1], [1]]))

    x_times = sum([simplify[i][0] for i in range(3)])

    # Modulo value - 2 char values of keys added together
    modulo_value = ord(key[9]) + ord(key[10])

    for sub_str in text:
        char_value = [ord(sub_str[i]) for i in range(3)]
        # C = (modulo_value * char[4] + char_value) / x_times
        c = math.floor((modulo_value * ord(sub_str[3]) + sum(char_value)) / x_times)
        decrypted_text += chr(c)

    return decrypted_text
