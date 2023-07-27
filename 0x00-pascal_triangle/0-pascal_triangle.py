#!/usr/bin/python3
"""Pascal triangle module"""


def pascal_triangle(n):
    """This function returns pascal triangle whose
    size is @n
    """
    pascal_list = []
    for i in range(n):
        tmp_list = []
        for j in range(i + 1):
            if j == 0 or j == i:
                tmp_list.append(1)
            else:
                tmp_list.append(
                        pascal_list[i - 1][j] + pascal_list[i - 1][j - 1])
        pascal_list.append(tmp_list)
    return pascal_list
