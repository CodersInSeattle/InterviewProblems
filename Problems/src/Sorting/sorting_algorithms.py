def counting_sort(nums, upper_bound):
    """Assumes nums in range [0, upper_bound)."""
    counts = [0] * upper_bound
    for val in nums:
        counts[val] += 1
    start = 0
    for i, count in enumerate(counts):
        for j in xrange(count):
            nums[start+j] = i
        start += count


def shellSort(array):
    gap = len(array) / 2
    while gap > 0:
        insertion_sort(array, gap)
        gap /= 2


def insertion_sort(array, gap=1):
    for i in xrange(gap, len(array)):
        val = array[i]
        j = i
        while j >= gap and array[j-gap] > val:
            array[j] = array[j-gap]
            j -= gap
        array[j] = val


def selection_sort(array):
    for i in xrange(len(array)):
        min_index = _min_index_starting_at(array, i)
        array[i], array[min_index] = array[min_index], array[i]


def _min_index_starting_at(array, begin):
    min_index, min_val = begin, array[begin]
    for i in xrange(begin, len(array)):
        if array[i] < min_val:
            min_index, min_val = i, array[i]
    return min_index


if __name__ == '__main__':
    l = [2, 2, 1, 1, 2, 0, 0, 2, 0]
    print counting_sort(l, 3)
