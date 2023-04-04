# Write a program that takes a string as input and checks if it is a palindrome (a word, phrase, or sequence that reads the same backward as forward).

def is_palindrome(test_str):
    reversed_str = ""
    for letter in reversed(test_str):
        reversed_str += letter

    if test_str == reversed_str:
        return True
    return False


check_string = "maths shtam"
is_check_palindrome = is_palindrome(check_string)
print(f"{check_string} is palindrome: {is_check_palindrome}")
