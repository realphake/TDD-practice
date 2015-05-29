import unittest

class testSuite(unittest.TestCase):

    def setUp(self):
        pass

    def testTautology(self):
        self.assertEqual(True,True)

unittest.main()

