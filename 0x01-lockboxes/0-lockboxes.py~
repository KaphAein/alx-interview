#!/usr/bin/python3
'''Pascal Triangle Module'''


def pascal_triangle(n):
    '''Creats a Pascal Triangle'''

    triangle = []
    if not isinstance(n, int) or n <= 0:
        return triangle
    elif n is None:
        return None

    for y in range(n):
        row = []

        for x in range(y+1):
            if (x == 0 or x == y):
                row.append(1)
            else:
                row.append(triangle[y-1][x-1] + triangle[y-1][x])
        triangle.append(row)

    return triangle
