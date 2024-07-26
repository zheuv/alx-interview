#!/usr/bin/python3

def pascal_triangle(n):
    matrice = []
    if n <= 0:
        return matrice
    for index in range(n):
        newRow = [1]
        if index > 0:
            lastRow = matrice[-1]
            for j in range(1, index):
                    newRow.append(lastRow[j] + lastRow[j-1])
            newRow.append(1)
        matrice.append(newRow)
    return matrice
