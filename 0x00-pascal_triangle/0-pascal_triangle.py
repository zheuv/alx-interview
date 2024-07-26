#!/usr/bin/python3
"""
pascal_triangle module
This module provides a function to generate
Pascal's Triangle up to a given number of rows.
"""


def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to n rows.
    Pascal's Triangle is a triangular array
    of the binomial coefficients.
    Each row represents the coefficients of
    the binomial expansion, where the outermost elements
    are 1, and each inner element is the sum of the two
    elements directly above it in the
    previous row.
    """
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
