# Import testing library
import unittest

# Import our program to test
import fibonacci

FILE = "fibonacciResults.txt"

class TestUM(unittest.TestCase):

    def setUp(self):
        pass

    def test_fibonacciNumbers(self):
        testResults = [
            fibonacci.fibonacci(),
            fibonacci.fibonacci(10, -1),
            fibonacci.fibonacci(10, 50),
            fibonacci.fibonacci(5, 5)
        ]
        trueFibonacci = [
            [0, 1, 1, 2, 3, 5, 8, 13, 21, 34],
            [0, 1, 1, 2, 3, 5, 8, 13, 21, 34],
            [55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181],
            [8, 13, 21, 34, 55]
        ]
        self.assertEqual(testResults, trueFibonacci)


    def test_faultyInputs(self):
        testResults = [
            fibonacci.fibonacci(),
            fibonacci.fibonacci("x", "x"),
            fibonacci.fibonacci(True, False),
            fibonacci.fibonacci("aaaa"),
            fibonacci.fibonacci(None,"eeeee")
        ]
        expectedResults = [
            [0, 1, 1, 2, 3, 5, 8, 13, 21, 34],
            [0, 1, 1, 2, 3, 5, 8, 13, 21, 34],
            [0, 1, 1, 2, 3, 5, 8, 13, 21, 34],
            [0, 1, 1, 2, 3, 5, 8, 13, 21, 34],
            [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        ]
        self.assertEqual(testResults, expectedResults)


    def throwsException_indexError(self):
        self.assertRaises(indexError, fibonacci)

    def test_succesfulOutput(self):
        fibonacci.fibonacci()
        file = open(FILE, "r")
        output = file.read()
        self.assertEqual(output, "[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]")
        file.close()

if __name__ == '__main__':
    unittest.main()
