#  Write a program that takes a list of integers as input and returns a new list with the integers sorted in descending order.

my_list = [1, 23, 22, 45, 654, 3, 67, 897, 652]


def sort_desc1(my_list):
    sorted_list = []
    sorted_list.append(my_list[0])

    for i in range(1, len(my_list)):
        number_in_list = my_list[i]
        for index, val in enumerate(sorted_list):
            if number_in_list > val:
                sorted_list.insert(index, number_in_list)
                break

    return sorted_list


def sort_desc2(my_list):
    return sorted(my_list, reverse=True)


sort_desc_list1 = sort_desc1(my_list)
sort_desc_list2 = sort_desc2(my_list)
print(sort_desc_list1)
print(sort_desc_list2)
