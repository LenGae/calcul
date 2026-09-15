from main import Calculator
import unittest


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_plus(self):
        self.assertEqual(self.calc.plus(5, 3), 8)

    def test_umn(self):
        self.assertEqual(self.calc.umn(4, 3), 12)

    def test_st(self):
        self.assertEqual(self.calc.st(10, 3), 7)

    def test_pod_success(self):
        self.assertEqual(self.calc.pod(10, 2), 5.0)

    def test_pod_by_zero(self):
        self.assertEqual(self.calc.pod(10, 0), "На ноль нельзя делить")
