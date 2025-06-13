import unittest
from average import calculate_average

class TestCalculateAverage(unittest.TestCase):

    #положительные числа
    def test_positive_numbers(self):
        self.assertEqual(calculate_average([1, 2, 3]), 2)
        self.assertEqual(calculate_average([10, 20, 30]), 20)

    #отрицательные числа
    def test_negative_numbers(self):
        self.assertEqual(calculate_average([-1, -2, -3]), -2)
        self.assertEqual(calculate_average([-5, -10, -15]), -10)

    #смешанные числа
    def test_mixed_numbers(self):
        self.assertEqual(calculate_average([-1, 0, 1]), 0)
        self.assertEqual(calculate_average([100, -100]), 0)

    #пустой
    def test_empty_list(self):
        self.assertIsNone(calculate_average([]))
        self.assertEqual(calculate_average([]), None)

if __name__ == '__main__':
    unittest.main()
