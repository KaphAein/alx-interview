#!/usr/bin/python3
'''Minimum Operations Modulus'''


def minOperations(n):
    '''Calculate the minimum number of operations to get exactly n 'H's'''
    if not isinstance(n, int):
        return 0

    if n <= 1:
        return 0

    operations = 0
    current = n

    for i in range(2, n + 1):
        while current % i == 0:
            operations += i
            current //= i

    for current > 1:
        operations += current

    return operations
