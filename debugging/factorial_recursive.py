#!/usr/bin/python3
import sys


def factorial(n):
    """
    Description: Compute the factorial of a non-negative integer using recursion.
    Parameters: n (int) - non-negative integer to compute the factorial for.
    Returns: int - factorial of n.
    """
    if n == 0:
        return 1
    return n * factorial(n - 1)


f = factorial(int(sys.argv[1]))
print(f)
