import unittest
import math

#Choose a positive number. If it's even, divide by two.
#If it's odd, triple it and add one. Keep doing that.
#Eventually, all numbers will reach 1.

class InvalidInputException(Exception): pass

class Collatzer():

    def convergesAt(self, number):
        if number <= 0 or number % 1 != 0:
            raise InvalidInputException
        elif number == 1:
            return 0
        elif number % 2 == 0:
            return self.convergesAt(number/2)+1
        else:
            return self.convergesAt(number*3+1)+1

class testSuite(unittest.TestCase):

    def setUp(self):
        self.collatzer = Collatzer()

    def testInvalidInput(self):
        with self.assertRaises(InvalidInputException):
            self.collatzer.convergesAt(0)
            self.collatzer.convergesAt(1.5)

    def testPowersOfTwo(self):
        self.assertEqual(self.collatzer.convergesAt(1),0)
        self.assertEqual(self.collatzer.convergesAt(2),1)
        self.assertEqual(self.collatzer.convergesAt(4),2)
        self.assertEqual(self.collatzer.convergesAt(5),5)
        self.assertEqual(self.collatzer.convergesAt(8),3)
        self.assertEqual(self.collatzer.convergesAt(10),6)
        self.assertEqual(self.collatzer.convergesAt(21),7)
        self.assertEqual(self.collatzer.convergesAt(106),12)
            
unittest.main()

