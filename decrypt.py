#!/usr/bin/env python


def decrypt(ciphertext, shift=0):
    """
    Decrypts a Caesar cipher encrypted message.
    :param ciphertext: The message to be encrypted
    :param shift: The number of positions to shift each letter
    """
    return ciphertext


if __name__ == "__main__":
    ciphertext = input("Message to decrypt: ")
    shift = int(input("Shift: "))
    print(decrypt(ciphertext, shift))
