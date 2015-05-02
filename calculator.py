import unittest

class StringCalculator():

    def product(self,listOfNumbers):
        product = 1
        for number in listOfNumbers:
            product *= number
        return product

    def castAllToFloat(self, listOfNumbers):
        return [self.calculate(n) for n in listOfNumbers]
    
    def calculate(self, calculation):
        if "+" in calculation:
            listOfNumbers = calculation.split("+")
            return sum( self.castAllToFloat(listOfNumbers) )
        if "*" in calculation:
            listOfNumbers = calculation.split("*")
            return self.product( self.castAllToFloat(listOfNumbers) )
        return float(calculation)

class testCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = StringCalculator()

    def testRepeatTwelve(self):
        self.assertEqual(self.calc.calculate("12"), 12)

    def testAddition(self):
        self.assertEqual(self.calc.calculate("12+1+2"),15)

    def testFloatCalling(self):
        self.assertEqual(self.calc.calculate("3.8"),3.8)
    
    def testMultiplication(self):
        self.assertEqual(self.calc.calculate("3*2*4"),24)

    def testFloatingPointNumbers(self):
        self.assertEqual(self.calc.calculate("3.8+2.3"),6.1)

    def testMixedProblem(self):
        self.assertEqual(self.calc.calculate("3+2*4"),11)

unittest.main()
