# Caesar Cipher

Create a program that can _encrypt_ or _decrypt_ a message using the [Caesar Cipher](https://en.wikipedia.org/wiki/Caesar_cipher).

If _encrypting_ a message, the program should:

- take as input:
  - the plaintext message to be encrypted
  - the shift or offset to be used
- return the encrypted or "ciphertext" message.

If _decrypting_ a message, the program should:

- take as input:
  - the ciphertext message to be decrypted
  - the shift or offset to be used
- return the decrypted or "plaintext" message.

## What's a Caesar Cipher?

A _cipher_ is a method of disguising a message by encoding it. The _Caesar Cipher_
is a type of substitution cipher where each letter in a message is 'shifted' a
certain number of places down or up the alphabet.

For example:

- with a shift of 1, A would be replaced by B, B would become C, and so on.
- with a shift of 3, D would be replaced by G, E would become H, and so on.

If the shift or offset extends past the end of the alphabet, the letter wraps
around to the beginning.

For example:

- if you shift Z by 1, you would get A.
- if you shift Y by 4, you would get C.

For our purposes, we will only be shifting letters. All other characters (numbers,
punctuation, spaces, etc.) should remain unchanged.

Thus the message "BUZZ OFF" encrypted with a shift of 2 would become "DWBB QHH".

## Getting started

Accept the assignment by following the link from our [course website](https://northridge.dev/game-dev).

You'll write the encryption function in `encrypt.py` and the decryption function
in `decrypt.py`. Run your code from the command line:

### Encrypting

```shell
python ./encrypt.py
```

### Decrypting

```shell
python ./decrypt.py
```

## Craftsmanship

For this problem set, focus on writing a comprehensive set of tests.

The `test_encrypt.py` and `test_decrypt.py` files each contain an example test
and further instructions. Ideally, you'll have a set of tests that, if they all
pass, will give you confidence that your program is working correctly.

Want to be a real _pro_? Write your tests first, then write the code to make them pass.

To run all the tests, use the command:

```shell
pytest
```

## How your code will be evaluated

For both the `encrypt` and `decrypt` functions:

- [ ] You've written tests for a wide variety of typical and edge cases.
- [ ] Your tests pass.

## Bonus

There are different strategies or algorithms for solving this problem.

- Implement a different algorithm, which may require using different data
  structures or control flow.
- Make sure your new implementation can pass the same tests as your original
  implementation.
- Compare the two. Which is better? Which is more efficient?
