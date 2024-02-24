#!/usr/bin/env python


def encrypt(plaintext, shift=0):
    """
    Uses the Caesar cipher to encrypt a plaintext message.
    :param plaintext: The message to be encrypted
    :param shift: The number of positions to shift each letter
    """
    return plaintext


if __name__ == "__main__":
    plaintext = input("Message to encrypt: ")
    shift = int(input("Shift: "))
    print(encrypt(plaintext, shift))
