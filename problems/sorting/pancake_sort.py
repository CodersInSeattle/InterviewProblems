"""
Given an unsorted array, sort the given array using only a flip() operation:
  flip(arr, i): Reverse arr from 0 to i
"""


def flip(arr, i):
    # Implemented only for testing
    low, high = 0, i
    while low < high:
        arr[low], arr[high] = arr[high], arr[low]
        low += 1
        high -= 1


def pancake_sort(arr):
    for i in xrange(len(arr)-1, -1, -1):
        best_index = _find_max_up_to(arr, i)
        flip(arr, best_index)
        flip(arr, i)
    return arr


def _find_max_up_to(arr, right_bound):
    best_index = 0
    max_val = None
    for i in range(right_bound + 1):
        if arr[i] > max_val:
            best_index = i
            max_val = arr[i]
    return best_index


if __name__ == '__main__':
    NUMS = [-3, 2, 23, 5, 8, 2, 9, 0, 0, -2, -4]
    print pancake_sort(NUMS)
