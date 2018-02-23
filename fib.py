"""
フィボナッチ数を返却する
・fib(0) = 0
・fib(1) = 1
・fib(n+2) = fib(n) + fib(n+1) (n ≧ 0)
"""

from unittest import TestCase


def fib(num):
    if num == 0 or num == 1:
        return num
    else:
        return fib(num - 1) + fib(num - 2)


class Test(TestCase):

    def test_fib1(self):
        """0を渡したら0を返すテスト"""
        expected = 0
        actual = fib(0)
        self.assertEquals(expected, actual)

    def test_fib2(self):
        """1を渡したら1を返すテスト"""
        expected = 1
        actual = fib(1)
        self.assertEquals(expected, actual)

    def test_fib3(self):
        """2を渡したら1を返すテスト"""
        expected = 1
        actual = fib(2)
        self.assertEquals(expected, actual)

    def test_fib4(self):
        """10を渡したら55を返すテスト"""
        expected = 55
        actual = fib(10)
        self.assertEquals(expected, actual)



