#!/usr/bin/python3
"""
Module for canUnlockAll function
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be unlocked.

    Each box may contain keys to other boxes.
    The function checks if all boxes can be
    unlocked starting from the first box (index 0).

    Parameters:
    boxes (list of lists of int): A list where
    each element is a list of integers representing keys.

    Returns:
    bool: True if all boxes can be unlocked, False otherwise.
    """
    keys = set()
    boxesLength = len(boxes)
    unlocked = 1

    for i in range(boxesLength):
        alreadyUpdatedI = False
        alreadyUpdatedJ = False
        j = boxesLength - (i + 1)
        if len(keys) != 0:
            if boxes[i] != "unlocked":
                if i in keys:
                    keys.update(set(boxes[i]))
                    alreadyUpdatedI = True
                    unlocked += 1
                    boxes[i] = "unlocked"
            if (boxes[j] != "unlocked") and (j != 0):
                if j in keys:
                    keys.update(set(boxes[j]))
                    alreadyUpdatedJ = True
                    unlocked += 1
                    boxes[j] = "unlocked"
        if alreadyUpdatedI is False:
            keys.update(set(boxes[i]))
        if alreadyUpdatedJ is False:
            keys.update(set(boxes[j]))
    if unlocked == boxesLength:
        return True
    return False
