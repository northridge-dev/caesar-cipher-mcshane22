[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-7f7980b617ed060a017424585567c406b6ee15c891e84e1186181d67ecf80aa0.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=14226652)
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
punctuation, spaces, etc.) should remain unchanged. Capital letters should remain
capitalized; lowercase letters should remain lowercase.

Thus the message "Buzz Off!" encrypted with a shift of 2 would become "Dwbb Qhh!".

## Getting started

Accept the assignment by following the link from our [course website](https://northridge.dev/game-dev).
Accepting the assignment will create for you a fork of this repository. Navigate
to your fork and use the "Code" button to open a Codespace.

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

## If you need a bit more help . . .

Read the [HELP I'M STUCK](/HELP_IM_STUCK.md) guide.

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

## How to submit

You'll have to get your code from your Codespace back to your
GitHub repository. We'll use a tool called `git`. Here's how:

1. In the terminal, `add` the files you've changed. The command, below, adds all
   files that that have been modified.

```shell
git add .
```

2. `commit` the changes you've added (you can change the message). "Committing"
   a set of changes is like taking a snapshot of all the changes you've made.
   The message is a summary of the changes to help future-you and others.

```shell
git commit -m "Completed the Caesar Cipher problem set"
```

3. `push` your changes to your GitHub repository. "Pushing" your changes sends
   the snapshot (the "commit") you created to GitHub, thus sharing it with
   anyone who has access to your repository.

```shell
git push
```

4. Navigate to your GitHub repository and confirm that the commit has been added
   to the commit history and your code reflects the changes you made.

## How your code will be graded

For both the `encrypt` and `decrypt` functions:

- You've written tests for a wide variety of typical and edge cases.
- Your tests pass.

## Bonus

You could use different strategies or algorithms to perform the encryption and
decryption.

- Implement a different algorithm, which may require using different data
  structures or control flow.
- Make sure your new implementation can pass the same tests as your original
  implementation.
- Compare the two. Which is better? Which is more efficient?
