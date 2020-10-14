"""
Author: Aidan Shannon
Program: sort_and_search_list.py

searches for object in list and sorts it
"""

animals = ["dog", "cat", "cow", "pig"]


def search_list():
    """
    searches for object in list, returns index or -1
    :return:
    """
    my_input = input("Which animal do you want to search?: ")
    if my_input in animals:
        return animals.index(my_input)
    else:
        return "-1"  # felt that return would work better with if statement


def sort_list():
    """
    sorts list alphabetically
    :return:
    """
    animals.sort()
    return animals  # return works with test statement


if __name__ == '__main__':
    test_list = search_list()
    print(test_list)
    print(sort_list())
