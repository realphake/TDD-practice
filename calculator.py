import unittest

class StringCalculator():
    
    def __init__(self):
        pass

    def product(self,numbersToMultiply):
        product = 1
        for number in numbersToMultiply:
            product *= number
        return product

    def calculate(self, calculation):
        if "+" in calculation:
            numbersToAdd = calculation.split("+")
            return sum( [int(i) for i in numbersToAdd] )
        if "*" in calculation:
            numbersToMultiply = calculation.split("*")
            return self.product([int(i) for i in numbersToMultiply])
        return int(calculation)

class testCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = StringCalculator()

    def testRepeatTwelve(self):
        self.assertEqual(self.calc.calculate("12"), 12)

    def testAddition(self):
        self.assertEqual(self.calc.calculate("12+1+2"),15)

    def testMultiplication(self):
        self.assertEqual(self.calc.calculate("3*2*4"),24)

unittest.main()
