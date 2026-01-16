#!/usr/bin/python3
"""
Minimum Operations
This module contains a function that calculate the fewest number
of operations need to result in exactly n 'H' characters in a file
"""


def minOperations(n):
    """
    Calculates the minimum number of operations to reach n H characters.
    Args:
        n (int): target number of H characters
    Returns:
        int: minimum number of operations, or 0 if impossible
    """
    if n < 2:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations
