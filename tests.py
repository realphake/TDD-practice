import unittest

class BowlingGame():

    pass

class testCalculator(unittest.TestCase) :
    
    def testNothing(self):
        self.assertEqual(1,1)
        self.assertTrue(True)
        
    def testCreateGame(self):
        game = BowlingGame()

unittest.main()


