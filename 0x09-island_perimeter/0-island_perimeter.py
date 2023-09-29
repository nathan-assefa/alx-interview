#!/usr/bin/python3
"""5-island_perimeter module"""


def island_perimeter(grid):
    """Returns the perimeter of the island described in grid"""
    if not grid:
        return (0)
    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]:
                perimeter += 4
                if i > 0 and grid[i - 1][j]:
                    perimeter -= 2
                if j > 0 and grid[i][j - 1]:
                    perimeter -= 2
    return perimeter
