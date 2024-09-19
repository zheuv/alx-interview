#!/usr/bin/python3
""" Doc for the n queens script """

import sys


def validate_input():
    """ Validate the input arguments. """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    return N


N = validate_input()


class Position():
    """ doc for position class """
    def __init__(self, XY, controlled, before=None, after=None):
        """ def for function """
        self.XY = XY
        self.after = after
        self.before = before
        self.controlled = controlled


def emptyBoard(N):
    """ def for function """
    chessBoard = set()
    for i in range(N):
        for j in range(N):
            chessBoard.add((i, j))
    return chessBoard


def controlledSquares(XY, N):
    """ doc for function """
    controlled = set()
    controlled.add(XY)  # Convert the list to a tuple
    for i in range(N):
        controlled.add((i, XY[1]))
        controlled.add((XY[0], i))
        if XY[0] + i < N and XY[1] + i < N:
            controlled.add((XY[0] + i, XY[1] + i))
        if XY[0] - i >= 0 and XY[1] + i < N:
            controlled.add((XY[0] - i, XY[1] + i))
        if XY[0] - i >= 0 and XY[1] - i >= 0:
            controlled.add((XY[0] - i, XY[1] - i))
        if XY[0] + i < N and XY[1] - i >= 0:
            controlled.add((XY[0] + i, XY[1] - i))
    return controlled


def check(XY, N, controlledByBefore, before, chessBoard, n):
    """ doc for function """
    controlled = controlledSquares(XY, N)
    if controlledByBefore is not None:
        controlled = controlled | controlledByBefore
    nonControlled = chessBoard.difference(controlled)
    if n == N - 1:
        position = Position(XY, controlled, before)
        before.after = position
        return
    if len(nonControlled) == 0:
        return
    n += 1
    position = Position(XY, controlled, before)
    for XY in nonControlled:
        check(XY, N, controlled, position, chessBoard, n)
        if position.after is not None:
            if before is None:
                return position
            before.after = position
            return


positions = []
chessBoard = emptyBoard(N)
for XY in chessBoard:
    position = check(XY, N, None, None, chessBoard, 0)
    if position is not None:
        solution = []
        while position:
            solution.append(list(position.XY))
            position = position.after
        if len(positions) > 0:
            for p in positions:
                e = 0
                for s in solution:
                    if (s not in p):
                        break
                    e += 1
                if e == N:
                    break
            if e != N:
                positions.append(solution)
        else:
            positions.append(solution)


for p in positions:
    print(p)
