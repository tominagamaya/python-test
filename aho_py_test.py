"""
世界のナベアツ
・数字を渡すと、渡した数字を文字列で返す
・3の倍数のときは阿呆になるので、「さぁ〜ん」と文字列を返す
・渡した数字に3が含まれるときは阿呆になるので、「さぁ〜ん」と文字列を返す
"""
from aho import aho_three


def test_aho1():
    """1を渡したら1を返すテスト"""
    expected = "1"
    actual = aho_three(1)

    assert expected == actual


def test_aho2():
    """3の倍数でアホになるテスト"""
    expected = "さぁ〜ん"
    actual = aho_three(6)

    assert expected == actual


def test_aho3():
    """3がつく数字でアホになるテスト"""
    expected = "さぁ〜ん"
    actual = aho_three(13)

    assert expected == actual
