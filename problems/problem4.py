# Write a program that takes a list of integers as input and prints the largest integer in the list.


def print_largest_integer_1(int_list):
    """
    This problem prints the largest integer from the list it receives 
    """
    largest_int = int_list[0]
    for num in int_list:
        if num > largest_int:
            largest_int = num

    print(f"Largest integer from the list {int_list} = {largest_int}")


def print_largest_integer_2(int_list):
    largest_int = max(int_list)
    print(f"Largest integer from the list {int_list} = {largest_int}")


print_largest_integer_1([1, 21, 43, 54, 21, 323, 12, 45, 65, 123, 454, 5657])
print_largest_integer_2([1, 21, 43, 54, 21, 323, 12, 45, 65, 123, 454, 5657, 21, 435, 3456, 345, 1, 3456, 134, 12341, 1341, 1341243, 1341234,
                        54, 52, 234, 1341234, 2354, 15, 454, 51, 134, 134, 544, 251454, 315, 45, 4252435, 425, 421, 4134, 134, 545, 631, 134, 134, 5452])
