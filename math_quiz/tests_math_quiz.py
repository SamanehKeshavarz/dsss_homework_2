import unittest
from math_quiz import RandomNumber, RandomOperator, Calculation


class TestMathGame(unittest.TestCase):

    def test_RandomNumber(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = RandomNumber(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_RandomOperator(self):
        operators = set()
        for _ in range(1000):
            operator = RandomOperator()
            operators.add(operator)
        self.assertEqual(operators, {'+', '-', '*'})

    def test_Calculation(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (10, 3, '*', '10 * 3', 30),
                (8, 4, '-', '8 - 4', 4)
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                problem, answer = Calculation(num1, num2, operator)
                self.assertEqual(problem, expected_problem)
                self.assertEqual(answer, expected_answer)

if __name__ == "__main__":
    unittest.main()
