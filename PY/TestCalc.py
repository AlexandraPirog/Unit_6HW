import unittest

from Calc import Calculate


class test_Calculate(unittest.TestCase):
    def biggerNum(self):
        self.assertEqual(Calculate.biggerNum([111, 6, 0], [2, 2,10]), "Первый список имеет большее среднее "
                                                                             "значение")
        self.assertEqual(Calculate.what_avg_is_bigger([5,7], [19, 26, 16]), "Второй список имеет большее среднее значение")
        self.assertEqual(Calculate.what_avg_is_bigger([9], [9,9]), "Средние значения равны")

    def test_avg_calculate(self):
        self.assertEqual(Calculate.avg_calculate([1, 5, 6]), 4)


if __name__ == '__main__':
    unittest.main()