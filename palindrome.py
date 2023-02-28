def is_palindrome(input_string):
    new_string = ""
    reverse_string = ""

    for x in input_string:
        if x != " ":
            new_string += x
            reverse_string = x + reverse_string

    if new_string.lower() == reverse_string.lower():
        return True

    return False

print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True