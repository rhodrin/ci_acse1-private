import pytest
import math
import numpy as np

from simple_functions import my_sum, factorial, sin_series


class TestSimpleFunctions(object):
    '''Class to test our simple functions are working correctly'''

    @pytest.mark.parametrize('iterable, expected', [
        ([8, 7, 5], 20),
        ((10, -2, 5, -10, 1), 4)
    ])
    def test_my_add(self, iterable, expected):
        '''Test our add function'''
        isum = my_sum(iterable)
        assert isum == expected

    @pytest.mark.parametrize('number, expected', [
        (5, 120),
        (3, 6),
        (1, 1)
    ])
    def test_factorial(self, number, expected):
        '''Test our factorial function'''
        answer = factorial(number)
        assert answer == expected

    @pytest.mark.parametrize(' pi_number, expected', [
        (0, 0),
        (math.pi, 0),
        (2*math.pi, 0)
    ])  
    def test_sin(self, pi_number, expected):
        """test sin"""
        sin_answer = sin_series(pi_number)
        assert np.isclose(sin_answer, expected, atol=1e-12)
