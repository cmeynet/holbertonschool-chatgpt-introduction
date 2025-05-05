#!/usr/bin/python3
import sys


def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result


if len(sys.argv) == 2:
    n = int(sys.argv[1])
    print(factorial(n))
else:
    print("Usage: ./script.py <entier>")
