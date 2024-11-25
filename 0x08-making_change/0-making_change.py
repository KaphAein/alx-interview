#!/usr/bin/python3
'''Making Change Module'''


def makeChange(coins, total):
    '''Making Change Function'''
    coins = sorted(coins, reverse=True)
    counter = 0
    for coin in coins:
        while total >= coin:
            total -= coin
            counter += 1
    if total > 0:
        return -1
    return counter
