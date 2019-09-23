import unittest
from fizzbuzz import fizzbuzz


class TestFizzbuzz(unittest.TestCase):
    def setUp(self):
        self.obj = fizzbuzz.FizzBuzz()

    def test_one(self):
        self.assertEqual(self.obj.print(1), str(1))

    def test_fizz(self):
        self.assertEqual(self.obj.print(3), 'Fizz')

    def test_buzz(self):
        self.assertEqual(self.obj.print(5), 'Buzz')

    def test_fizzbuzz(self):
        self.assertEqual(self.obj.print(15), 'FizzBuzz')


class TestInput(unittest.TestCase):
    def setUp(self):
        self.func = fizzbuzz.FizzBuzz()

    def test_valid_input(self):
        self.assertTrue(self.func.isValidCountableNumber(1))
        self.assertFalse(self.func.isValidCountableNumber(0))
        self.assertFalse(self.func.isValidCountableNumber(-1))


if __name__ == '__main__':
    unittest.main()
