"""
bit operations: ~, &, |, ^, >>, <<

Python 3 warning - this file is in python 3...

Problem 1:
    Given an integer, find the number of bits set.

Problem 2:
    Check if a given number is sparse or not
    A number is said to be a sparse number if in binary representation of the number no two or more consecutive bits are set. Write a function to check if a given number is Sparse or not.

    example:
    01010101 ==> sparse
    000001   ==> sparse
    001100   ==> not sparse

Problem 3:
    http://www.geeksforgeeks.org/find-profession-in-a-hypothetical-special-situation/

    Consider a special family of Engineers and Doctors with following rules :
    1. Everybody has two children.
    2. First child of an Engineer is an Engineer and second child is a Doctor.
    3. First child of an Doctor is Doctor and second child is an Engineer.
    4. All generations of Doctors and Engineers start with Engineer.

    We can represent the situation using below diagram:
                E
           /        \
          E          D
        /   \       /  \
       E     D     D    E
      / \   / \   / \   / \
     E   D D   E  D  E  E  D

    Given level and position of a person in above ancestor tree, find profession of the person.

    Examples:

    Input : level = 4, pos = 2
    Output : Doctor

    Input : level = 3, pos = 4
    Output : Engineer

    1
    10
    1001
    10010110

"""


def bit_count(x):
    """
    Problem 1:
        Given an integer x, return the number of bits set in the integer.

    ----------
    explanation:
        x - 1 => flips all bits in x up to the most right set bit
        x & (x - 1): remove the last set bit for x.

        therefore, repetitively set x = x & (x - 1), until x = 0, allows calculation of number of set bits in x.

    example:
        x     = 1010
        x - 1 = 1001
        &     = 1000 <== new x

        x     = 1000
        x - 1 = 0111
        &     = 0000 <=== new x

        new x ==> 0
        number of iteration ==> 2
        number of bits set in x ==> 2
    -----------
    does it work for negative numbers?

    """
    if x < 0:
        x = -x

    count = 0
    # get rid of one 1 at a time
    while x != 0:
        x &= (x - 1)
        count += 1
    return count


def is_power_of_two(x):
    """
    Return true if x is power of 2.
    ------------------
    explanation:
        2 -> 10
        4 -> 100
        6 -> 1000

        power of 2 ==> 1...0

        power of 2 - 1 ==> 0...1

        & ==> 0
    """
    return int(x) == x and x >= 1 and x & (x - 1) == 0


def is_power_of_four(x):
    """
    Usually a follow up of `is_power_of_two`.

    Return true if x is power of 4.
    -------
        1  ==> 1
        4  ==> 100
        16 ==> 10000
        64 ==> 1000000
        ....

        not only has to be 1...0, but the 1 must be on the odd position.

        ==> mask with 1010101010..etc.
        how?
    """
    return int(x) == x and x > 1 and x & (x - 1) == 0 and x & 0x55555555 != 0


def is_sparse(x):
    """
    Given a number x, returns true if it is sparse and false otherwise.
    -----
    explanation:

    if there is an `11` in a number, shift one digit and there will still be an 1
    overlapping.
    x       = 0110000
    x >> 1  = 0011000
                ^ overlaps
    &       = 0010000  ==> not zero.
    """
    if x < 0:
        x = -x
    return (x & (x >> 1)) == 0


def get_profession(level, position):
    """
    Given the level and position of the person from the special family (see Problem 3), returns the profession of the
    person.
    :return: 'E' if he/she is an engineer and 'D' if he/she is a doctor.
    """

    if level < 1:
        return ValueError('Level must be bigger than 0')
    if not 0 < position <= 2 ** (level - 1):
        return ValueError('Invalid position: {}'.format(position))

    # 1 for engineer
    generation = 1
    for i in range(0, level - 1):
        number_of_bits = 2 ** i
        generation = (generation >> number_of_bits) + ~generation

    # find out the position'th bit is set or not
    profession = (generation >> (generation.bit_length() - position)) % 2
    if profession == '1':
        return 'E'
    return 'D'
