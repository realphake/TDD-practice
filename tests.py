import unittest

class BowlingGame():

    def __init__(self):
        self.score = 0

    def roll(self, pins):
        self.score += pins

    def calculateScore(self):
        return self.score

class testCalculator(unittest.TestCase) :

    def rollBalls(self, balls, pinsPerBall):
        for x in range(0,balls):
            self.game.roll(pinsPerBall)

    def setUp(self):
        self.game = BowlingGame()

    def testGutterGame(self):
        self.rollBalls(20, 0)
        self.assertEqual(self.game.calculateScore(),0)
        
    def testAllOnes(self):
        self.rollBalls(20, 1)
        self.assertEqual(self.game.calculateScore(),20)

unittest.main()


