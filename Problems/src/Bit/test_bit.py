import random

import bit


class TestBit(object):
    
    def _bit_count(self, x):
        return bin(x).count('1')

    def test_bit_count_zero(self):
        assert self._bit_count(0) == bit.bit_count(0)

    def test_bit_count_negative(self):
        assert self._bit_count(-20) == bit.bit_count(-20) 

    def test_bit_count_positive(self):
        assert self._bit_count(90) == bit.bit_count(90)

    def test_bit_count_random(self):
        random_int = random.randint(-9999999, 9999999)
        assert self._bit_count(random_int) == bit.bit_count(random_int)

