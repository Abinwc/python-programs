""" Write a program that takes a list of integers as input and returns a new list with only the even integers from the original list."""


def return_even_number(total_list):
    even_num_list = []
    for num in total_list:
        if num % 2 == 0:
            even_num_list.append(num)

    return even_num_list


print(return_even_number([1, 2, 3, 4, 56, 6, 7, 7, 5, 4, 3]))
