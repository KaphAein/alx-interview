#!/usr/bin/python3
'''Making Change Module'''


def makeChange(coins, total):
    '''Making Change Function'''
    if total <= 0:
        return 0

    coins = sorted(coins, reverse=True)
    counter = 0
    for coin in coins:
        count, total = divmod(total, coin)
        counter += count
    return counter if total == 0 else -1
