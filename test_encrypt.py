from encrypt import encrypt


def test_example():
    assert encrypt("BUZZ OFF!", 2) == "DWBB QHH!"


"""
Add test cases. Use the example, above, as a model.

Think about what ways that your `encrypt` function could fail.
For each, write a test case that will fail if your function 
does not handle that case correctly.

For each test case, write a new function. It's name MUST
start with "test_", for example, "test_encrypt_empty_string"
or "test_encrypt_message_with_punctuation". Choose descriptive
names -- names that describe what the test is checking.

Each function should contain at least one `assert` statement.
The basic format is:
  assert encrypt("<plaintext-to-encrypt>", <shift>) == "<expected-output>"
"""
