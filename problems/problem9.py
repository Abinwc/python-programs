# Write a program that takes two strings as input and concatenates them (joins them together) into a new string.

def concatenate_two_string1(str1, str2):
    return str1+str2


def concatenate_two_string2(str1, str2):
    return f"{str1}{str2}"


final_str1 = concatenate_two_string1('Hello', 'world')
final_str2 = concatenate_two_string2("Hello", "world")
print(final_str1)
print(final_str2)
