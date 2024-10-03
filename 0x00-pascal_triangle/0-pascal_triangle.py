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
    row = [1]
    
    if (y > 0):
      for x in range(1, y):
        row.append(triangle[y-1][x-1] + triangle[y-1][x])
      row.append(1)
    triangle.append(row)
  return triangle
