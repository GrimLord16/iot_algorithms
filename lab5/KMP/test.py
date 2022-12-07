import unittest

from kmp import kmp_search


class MyTestCase(unittest.TestCase):
    def test_kmp(self) -> None:
        with open("test/test_the_least_runtime.txt") as file:
            text1: str = file.readline()
            print(len(text1))
        with open("test/test_medium_runtime.txt") as file:
            text2: str = file.readline()
            print(len(text2))
        with open("test/test_the_worst_option.txt") as file:
            text3: str = file.readline()
            print(len(text3))
        result: list[int] = [i for i in range(0, 1044)]

        self.assertEqual(kmp_search(text1, "aaaaaaaaaaaaaaaaaaaaaaa"), result)
        self.assertEqual(kmp_search(text2, "abababababababababdf"), [162, 254])
        self.assertEqual(kmp_search(text3, "acaacaacaacadf"), [168, 260])
        self.assertEqual(kmp_search(text3, "lyigliykufkurukf"), -1)


if __name__ == '__main__':
    unittest.main()
