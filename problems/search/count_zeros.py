"""
Given a matrix M of size X*Y, filled with integers.
Rows and columns of the matrix are sorted in ascending order.
Find the number of zeros in the matrix.
"""


def count_zeros(matrix):
    """Returns the number of zeros in a matrix."""
    row_idx, col_idx = 0, len(matrix[0])-1
    result = 0
    while row_idx <= len(matrix)-1 and col_idx >= 0:
        current_val = matrix[row_idx][col_idx]
        if current_val >= 0:
            if current_val == 0:
                result += 1
            col_idx -= 1
        else:
            row_idx += 1
    return result


if __name__ == '__main__':
    M1 = [[-4, -3, -2, 0, 3],
          [-3, -1, 0, 4, 5],
          [-2, 0, 3, 8, 10],
          [-1, 1, 7, 9, 12]]
    assert count_zeros(M1) == 3
    M2 = [[10, 20, 30, 40],
          [15, 25, 35, 45],
          [27, 29, 37, 48],
          [32, 33, 39, 50]]
    assert count_zeros(M2) == 0
