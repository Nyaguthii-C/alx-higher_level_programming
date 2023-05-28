#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in range(0, len(matrix)):
        for j in matrix[i]:
            new_matrix.append(j**2)
    return new_matrix
