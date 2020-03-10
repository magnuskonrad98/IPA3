import unittest
from sample import fizzbuzz

class MyFirstTests(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(fizzbuzz(5), 'Buzz')
        self.assertEqual(fizzbuzz(6), 'Fizz')
        self.assertEqual(fizzbuzz(15), 'FizzBuzz')
        self.assertEqual(fizzbuzz(8), "8")



if __name__ == '__main__':
    unittest.main()