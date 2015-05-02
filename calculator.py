import unittest

class StringCalculator():
    
    def __init__(self):
        pass

    def calculate(self, calculation):
        if "+" in calculation:
            parts = calculation.split("+")
            return sum( [int(i) for i in parts] )
        return int(calculation)

class testCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = StringCalculator()

    def testRepeatZero(self):
        self.assertEqual(self.calc.calculate("0"), 0)

    def testRepeatTwelve(self):
        self.assertEqual(self.calc.calculate("12"), 12)

    def testOnePlusTwo(self):
        self.assertEqual(self.calc.calculate("1+2"),3)

    def testSumOfThreeNumbers(self):
        self.assertEqual(self.calc.calculate("12+1+2"),15)

unittest.main()
