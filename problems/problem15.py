# Write a program that takes a list of integers as input and returns a new list with only the prime integers from the original list.

def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def return_only_prime_number(my_list):
    my_prime_list = []
    for num in my_list:
        if is_prime(num):
            my_prime_list.append(num)

    return my_prime_list


my_prime_list = return_only_prime_number([3, 4, 5, 6, 7, 8, 9, 13, 16])
print(my_prime_list)
