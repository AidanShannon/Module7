"""
Author: Aidan Shannon
Program: basic_list.py

takes your inputs and sticks them into a list
"""


def make_list():
    """
    makes list for user's inputs
    :return:
    """
    u_list = []
    for i in range(0, 3):
        u_input = int(get_input())
        u_list.insert(i, u_input)
    return u_list


def get_input():
    """
    gets inputs for the list
    :return:
    """
    u_input = input("Give me a number: ")
    return u_input


if __name__ == '__main__':
    test_list = make_list()
    print(test_list)
