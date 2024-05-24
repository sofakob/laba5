import unittest
from laba5 import add 

class TestAddFunction(unittest.TestCase):
    
    def test_add_integers(self):
        """Тест додавання цілих чисел."""
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, -1), -2)
        self.assertEqual(add(-1, 1), 0)
    
    def test_add_floats(self):
        """Тест додавання чисел з плаваючою комою."""
        self.assertAlmostEqual(add(1.5, 2.5), 4.0)
        self.assertAlmostEqual(add(-1.5, -2.5), -4.0)
        self.assertAlmostEqual(add(-1.5, 2.5), 1.0)

    def test_add_integer_and_float(self):
        """Тест додавання цілого числа і числа з плаваючою комою."""
        self.assertAlmostEqual(add(1, 2.5), 3.5)
        self.assertAlmostEqual(add(-1, 2.5), 1.5)
        self.assertAlmostEqual(add(1.5, 2), 3.5)

    def test_add_zero(self):
        """Тест додавання нуля."""
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(0, 5), 5)
        self.assertEqual(add(-5, 0), -5)

if __name__ == '__main__':
    unittest.main()