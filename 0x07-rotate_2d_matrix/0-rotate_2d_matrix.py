#!/usr/bin/python3
'''2D Matix Module'''


def rotate_2d_matrix(matrix):
    '''2D Matrix Function'''
    n = len(matrix)

    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] =  matrix[j][i], matrix[i][j]

    for row in matrix:
        row.reverse()