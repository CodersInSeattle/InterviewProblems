import random
import math

from Problems.bit import bit


RANDOM_TEST_ITERATION = 5


class TestBitCount(object):

    @staticmethod
    def _bit_count_naive(x):
        return bin(x).count('1')

    def test_bit_count_zero(self):
        assert bit.bit_count(0) == self._bit_count_naive(0) == 0

    def test_bit_count_negative(self):
        assert bit.bit_count(-20) == self._bit_count_naive(-20) == 2   # '-0b10100'

    def test_bit_count_positive(self):
        assert bit.bit_count(90) == self._bit_count_naive(90) == 4  # '0b1011010'

    def test_bit_count_random(self):

        for i in range(RANDOM_TEST_ITERATION):
            random_int = random.randint(-9999999, 9999999)
            assert bit.bit_count(random_int) == self._bit_count_naive(random_int), \
                'failed to calculate bit set for {}'.format(random_int)


class TestIsSparse(object):

    @staticmethod
    def _is_sparse_naive(x):
        return not ('11' in bin(x))

    def test_is_sparse_zero(self):
        assert bit.is_sparse(0) == self._is_sparse_naive(0) == True

    def test_is_sparse_negative(self):
        assert bit.is_sparse(-1) == self._is_sparse_naive(-1) == True
        assert bit.is_sparse(-3) == self._is_sparse_naive(-3) == False

    def test_is_sparse_positive(self):
        assert bit.is_sparse(1) == self._is_sparse_naive(1) == True
        assert bit.is_sparse(3) == self._is_sparse_naive(3) == False

    def test_is_sparse_random(self):
        for i in range(RANDOM_TEST_ITERATION):
            random_int = random.randint(-99999999, 99999999)
            assert bit.is_sparse(random_int) == self._is_sparse_naive(random_int), \
                'failed to calculate bit set for {}'.format(random_int)


class TestIsPowerOfTwo(object):

    @staticmethod
    def _is_power_of_two_naive(x):
        if x < 0 or int(x) != x:
            return False
        power = math.log(x, 2)
        return power == int(power)

    def test_is_power_of_two_negative(self):
        assert not bit.is_power_of_two(-1)

    def test_is_power_of_two_zero(self):
        assert not bit.is_power_of_two(0)

    def test_is_power_of_two_one(self):
        assert bit.is_power_of_two(1)

    def test_is_power_of_two_random_true(self):
        for i in range(RANDOM_TEST_ITERATION):
            random_int = random.randint(0, 999999999)
            assert bit.is_power_of_two(2 ** random_int), \
                'failed to identify power of 2 with power = {}'.format(random_int)

    def test_is_power_of_two_random_int(self):
        for i in range(RANDOM_TEST_ITERATION):
            random_int = random.randint(-99999999, 99999999)
            assert bit.is_power_of_two(random_int) == self._is_power_of_two_naive(random_int), \
                'failed to identify random power of 2 for {}'.format(random_int)

    def test_is_power_of_two_random_float(self):
        for i in range(RANDOM_TEST_ITERATION):
            random_float = random.random() * random.randint(-99999999, 99999999)
            assert bit.is_power_of_two(random_float) == self._is_power_of_two_naive(random_float), \
                'failed to identify power of 2 for {}'.format(random_float)


class BitGetProfession(object):
    """
                E
           /        \
          E          D
        /   \       /  \
       E     D     D    E
      / \   / \   / \   / \
     E   D D   E  D  E  E  D
    """

    @staticmethod
    def _get_profession_naive(level, position):
        professions = {
            (1, 1): 'E',
            (2, 1): 'E', (2, 2): 'D',
            (3, 1): 'E', (3, 2): 'D', (3, 3): 'D', (3, 4): 'E',
            (4, 1): 'E', (4, 2): 'D', (4, 3): 'D', (4, 4): 'E',
            (4, 5): 'D', (4, 6): 'E', (4, 7): 'E', (4, 8): 'D'
        }

        return professions[(level, position)]

    def test_get_profession_random(self):

        for i in range(RANDOM_TEST_ITERATION):
            random_level = random.randint(1, 4)
            random_position = random.randint(1, 2 ** (random_level - 1))

            assert bit.get_profession(random_level, random_position) == self._get_profession_naive(
                random_level, random_position), 'failed for level = {}, position = {}'.format(
                random_level, random_position)
