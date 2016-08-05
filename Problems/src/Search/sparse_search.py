def search_for_string(list_of_strings, target):
    '''Finds the index of target in list_of_strings.

    This methods assumes that
        1) target != ''
        2) target is guaranteed to exist in list_of_strings
    '''
    if not list_of_strings:
        return -1
    left, right = 0, len(list_of_strings) - 1
    while left <= right:
        mid = left + (right-left) / 2
        if list_of_strings[mid] == '':
            mid = _find_closest_nonempty_in_range(list_of_strings, mid, left,
                                                  right)
        if list_of_strings[mid] == target:
            return mid
        elif list_of_strings[mid] < target:
            left = mid + 1
        else:
            right = mid - 1


def _find_closest_nonempty_in_range(strings, index, low, high):
    left_candidate, right_candidate = index - 1, index + 1
    while left_candidate >= low or right_candidate <= high:
        if left_candidate >= low and strings[left_candidate] != '':
            return left_candidate
        elif right_candidate <= high and strings[right_candidate] != '':
            return right_candidate
        else:
            left_candidate -= 1
            right_candidate += 1


if __name__ == '__main__':
    STRINGS_EVEN_LEN = ['a', '', 'b', '']
    print search_for_string(STRINGS_EVEN_LEN, 'a')
    print search_for_string(STRINGS_EVEN_LEN, 'b')
    STRINGS_ODD_LEN = ['a', '', 'b']
    print search_for_string(STRINGS_ODD_LEN, 'a')
    print search_for_string(STRINGS_ODD_LEN, 'b')
