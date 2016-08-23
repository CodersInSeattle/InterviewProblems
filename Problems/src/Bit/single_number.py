
NUMS = [1, 2, 3, 2, 3, 1, 4, 4, 9]
1 ^ 2 ^ 3 ^ 2 ^ 3 = 1 ^ (2 ^ 2) ^ (3 ^ 3) = 1 ^ 0 ^ 0 = 1

0 ^ x = x
x ^ x = 0


[1, 2, 3, 2, 4, 3]
XOR everything:  1 ^ 4 = 101 (identifier)
group1: [5, 2, 3, 2, 3,0] => 1
group2: [4] => 4


def single_number_map(nums):
    counts = {}
    for n in nums:
        if n not in counts:
            counts[n] = 0
        else:
            counts[n] += 1
    for num, count in counts.iteritems():
        if count == 1:
            return num


def single_number_set(nums):
    appeared = set()
    for n in nums:
        try:
            appeared.pop(n)
        except KeyError:
            appeared.add(n)
    return appeared.pop()

def single_number_sort(nums):
    nums_sorted = sorted(nums)
    for i in xrange(1, len(nums)):
        if nums[i] == nums[i-1]:
            continue
        elif i < len(nums) - 1 and nums[i] == nums[i+1] :
            return nums[i-1]
        else:
            nums[i]

def single_number_bit(nums):
    return reduce(?, nums)




















