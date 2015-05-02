import unittest

class BowlingGame():

    def roll(self, pins):
        pass

class testCalculator(unittest.TestCase) :

    def setUp(self):
        self.game = BowlingGame()
        
    def testNothing(self):
        self.assertEqual(1,1)
        self.assertTrue(True)

    def testCanRoll(self):
        self.game.roll(1)

unittest.main()


