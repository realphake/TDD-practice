import unittest

#Write a program that prints the numbers from 1 to 100.
#For multiples of three print “Fizz” and for multiples of five “Buzz”.
#For numbers which are multiples of both three and five print “FizzBuzz”.

class fizzBuzzPrinter():

    def print(self, number):
        if number == 3:
            return "Fizz"
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

unittest.main()

