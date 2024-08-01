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
    keysI = set()
    keysJ = set()
    unlockedBoxes = {0}
    boxesLength = len(boxes)

    for i in range(boxesLength):
        j = boxesLength - (i + 1)
        if len(keysI) != 0:
            if (i not in unlockedBoxes) and (i in keysI):
                unlockedBoxes.add(i)
        if len(keysJ) != 0:
            if (j not in unlockedBoxes) and (j != 0) and (j in keysJ):
                unlockedBoxes.add(j)
        keysI.update(set(boxes[i]))
        keysJ.update(set(boxes[j]))
    if len(unlockedBoxes) == boxesLength:
        return True
    return False
