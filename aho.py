"""
世界のナベアツ
・数字を渡すと、渡した数字を文字列で返す
・3の倍数のときは阿呆になるので、「さぁ〜ん」と文字列を返す
・渡した数字に3が含まれるときは阿呆になるので、「さぁ〜ん」と文字列を返す
"""
from unittest import TestCase


def aho_three(num):
    """3の倍数と、3の値がつくときだけアホになる関数"""
    if num % 3 == 0 or "3" in str(num):
        return "さぁ〜ん"
    else:
        return str(num)


class Test(TestCase):

    def test_aho1(self):
        """1を渡したら1を返すテスト"""
        expected = "1"
        actual = aho_three(1)

        self.assertEquals(expected, actual)

    def test_aho2(self):
        """3の倍数でアホになるテスト"""
        expected = "さぁ〜ん"
        actual = aho_three(6)

        self.assertEquals(expected, actual)

    def test_aho3(self):
        """3がつく数字でアホになるテスト"""
        expected = "さぁ〜ん"
        actual = aho_three(13)

        self.assertEquals(expected, actual)
