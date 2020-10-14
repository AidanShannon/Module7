import array as arr

"""
Author: Aidan Shannon
Program: sort_and_search_list.py

searches for object in list and sorts it
"""

numbers = arr.array('d', [30.5, 15.5, 11.5, 20.5])


def search_array():
    pass


def sort_array():
    """
    sorts array numerically
    :return:
    """
    for i in range(0, len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] > numbers[j]:
                temp = numbers[i]
                numbers[i] = numbers[j]
                numbers[j] = temp
    return numbers  # return works with test statement


if __name__ == '__main__':
    test_array = search_array()
    print(test_array)
    sorted_array = sort_array()
    print(sorted_array)
