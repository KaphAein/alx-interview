#!/usr/bin/python3
'''Island Perimeter Module'''


def island_perimeter(grid):
    '''Island Perimeter Function'''
    if not grid or not isinstance(grid, list):
        return 0

    perimeter = 0
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == 1:
                perimeter += 4

                if x > 0 and grid[x - 1][y]:
                    perimeter -= 1
                if x < len(grid) - 1 and grid[x + 1][y]:
                    perimeter -= 1
                if y > 0 and grid[x][y - 1]:
                    perimeter -= 1
                if y < len(grid[0]) -1 and grid[x][y + 1]:
                    perimeter -= 1
    return perimeter
