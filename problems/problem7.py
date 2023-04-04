# Write a program that takes a list of integers as input and squares each value in the original list and store it in the original list.


def square_list(my_list):
    for index, num in enumerate(my_list):
        my_list.pop(index)
        my_list.insert(index, num*num)


my_int_list = [1, 2, 3, 4, 5]
square_list(my_int_list)
print(my_int_list)
