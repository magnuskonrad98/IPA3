import unittest
from sample import fizzbuzz

class MyFirstTests(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(fizzbuzz(5), 'Buzz')
        self.assertEqual(fizzbuzz(25), 'Buzz')
        self.assertEqual(fizzbuzz(55), 'Buzz')
        self.assertEqual(fizzbuzz(100), 'Buzz')

        self.assertEqual(fizzbuzz(6), 'Fizz')
        self.assertEqual(fizzbuzz(24), 'Fizz')
        self.assertEqual(fizzbuzz(48), 'Fizz')
        self.assertEqual(fizzbuzz(99), 'Fizz')

        self.assertEqual(fizzbuzz(15), 'FizzBuzz')
        self.assertEqual(fizzbuzz(45), 'FizzBuzz')
        self.assertEqual(fizzbuzz(405), 'FizzBuzz')
        self.assertEqual(fizzbuzz(4005), 'FizzBuzz')

        self.assertEqual(fizzbuzz(8), '8')
        self.assertEqual(fizzbuzz(43), '43')
        self.assertEqual(fizzbuzz(326), '326')
        self.assertEqual(fizzbuzz(686), '686')


if __name__ == '__main__':
    unittest.main()