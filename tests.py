import unittest

class BowlingGame():

    def __init__(self):
        self.allRolls = []

    def roll(self, pins):
        self.allRolls.append(pins)

    def scoreInFrame(self, frameStart):
        return self.allRolls[frameStart] + self.allRolls[frameStart+1]

    def isSpare(self, frameStart):
        return self.scoreInFrame(frameStart) >= 10

    def calculateScore(self):
        score = 0
        for frameStart in range(0,len(self.allRolls),2):
            score += self.scoreInFrame(frameStart)
            if self.isSpare(frameStart):
                score += self.allRolls[frameStart+2]
        return score

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

    def testOneSpare(self):
        self.rollBalls(2,5)
        self.rollBalls(1,7)
        self.rollBalls(17,0)
        self.assertEqual(self.game.calculateScore(),24)

unittest.main()


