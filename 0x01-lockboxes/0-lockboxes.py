#!/usr/bin/python3
""" Write a method that determines if all the boxes can be opened. """


def canUnlockAll(boxes):
    """ return True if all the boxes have keys """
    # Number of boxes
    n = len(boxes)

    # Set to keep track of visited boxes
    visited = set()

    # Stack for DFS
    stack = [0]  # Start with the first box (index 0)

    while stack:
        box = stack.pop()  # Get the next box to visit

        # Mark the current box as visited
        visited.add(box)

        # Check the keys in the current box
        for key in boxes[box]:
            # If we find a key to a new box, add it to the stack
            if key not in visited and key < n:
                stack.append(key)

    # If we have visited all boxes, return True, else return False
    return len(visited) == n
