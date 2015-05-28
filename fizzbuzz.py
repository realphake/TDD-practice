import unittest

#Write a program that prints the numbers from 1 to 100.
#For multiples of three print “Fizz” and for multiples of five “Buzz”.
#For numbers which are multiples of both three and five print “FizzBuzz”.

class fizzBuzzPrinter():

    def print(self, number):
        if number % 3 == 0 and number % 5 == 0:
            return "FizzBuzz"
        if number % 3 == 0:
            return "Fizz"
        elif number % 5 == 0:
            return "Buzz"
        else:
            return str(number)

class testSuite(unittest.TestCase):

    def setUp(self):
        self.fizzBuzzPrinter = fizzBuzzPrinter()

    def testPrintOne(self):
        self.assertEqual(self.fizzBuzzPrinter.print(1),"1")

    def testPrintTwo(self):
        self.assertEqual(self.fizzBuzzPrinter.print(2),"2")

    def testPrintThreeAsFizz(self):
        self.assertEqual(self.fizzBuzzPrinter.print(3),"Fizz")

    def testPrintFiveAsBuzz(self):
        self.assertEqual(self.fizzBuzzPrinter.print(5),"Buzz")

    def testPrintSixAsFizz(self):
        self.assertEqual(self.fizzBuzzPrinter.print(6),"Fizz")

    def testPrintTenasBuzz(self):
        self.assertEqual(self.fizzBuzzPrinter.print(10),"Buzz")

    def testPrintFifteenAsFizzBuzz(self):
        self.assertEqual(self.fizzBuzzPrinter.print(15),"FizzBuzz")

    def testPrintThirtyAsFizzBuzz(self):
        self.assertEqual(self.fizzBuzzPrinter.print(30),"FizzBuzz")

unittest.main()

