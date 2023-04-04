# Write a program that takes a list of integers as input and returns the sum of all the even integers in the list.

def sum_of_even_nums1(my_list):
    sum = 0
    for val in my_list:
        if val % 2 == 0:
            sum += val

    return sum


def sum_of_even_nums2(my_list):
    """
    Using list comprehension technique
    """
    even_nums = [num for num in my_list if num % 2 == 0]
    return sum(even_nums)


sum1 = sum_of_even_nums1([2, 4, 6, 8, 1, 2])
sum2 = sum_of_even_nums2([2, 4, 6, 8, 1, 2])
print(sum1)
print(sum2)
