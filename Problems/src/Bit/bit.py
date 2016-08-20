"""
Problem:
    Given an integer, find the number of bits set. 
"""

def bit_count(x):
    """
    Given an integer x, return the number of bits set in the integer.
    """
    if x < 0:
        x = -x

    count = 0
    while x != 0:
        x = x & (x - 1)
        count += 1
    return count


