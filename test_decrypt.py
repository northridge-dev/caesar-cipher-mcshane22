from decrypt import decrypt


def test_example():
    assert decrypt("Dwbb Qhh!", 2) == "Buzz Off!"


"""
Add test cases. Use the example, above, as a model.

Think about what ways that your `decrypt` function could fail.
For each, write a test case that will fail if your function 
does not handle that case correctly.

For each test case, write a new function. It's name MUST
start with "test_", for example, "test_decrypt_empty_string"
or "test_decrypt_message_with_punctuation". Choose descriptive
names -- names that describe what the test is checking.

Each function should contain at least one `assert` statement.
The basic format is:
  assert decrypt("<plaintext-to-encrypt>", <shift>) == "<expected-output>"
"""
