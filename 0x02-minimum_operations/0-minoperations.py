#!/usr/bin/python3
'''Main file for copy/paste algorithm'''


def minOperations(n):
    '''Calculates the minimum number of operations to get exactly n 'H' characters'''

    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        # Keep dividing `n` by the smallest divisor until it no longer divides cleanly
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        # Move to the next possible divisor
        divisor += 1

    return operations
