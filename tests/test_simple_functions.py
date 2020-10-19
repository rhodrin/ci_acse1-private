import numpy as np
import pytest
from simple_functions import my_sum, factorial, gauss


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


class TestGauss(object):
    """ Class for testing the Gaussian elimination algorithm """
    def test_one(self):
        a = [[2, 9, 4], [7, 5, 3], [6, 1, 8]]
        b = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        det, c = gauss(a, b)

        assert det == -360.0
        assert np.allclose(c, [[-0.10277777777777776, 0.18888888888888888,
                                -0.019444444444444438],
                               [0.10555555555555554, 0.02222222222222223,
                                -0.061111111111111116],
                               [0.0638888888888889, -0.14444444444444446,
                                0.14722222222222223]])
