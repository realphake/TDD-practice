import unittest

class BowlingGame():

    def __init__(self):
        self.allRolls = []

    def roll(self, pins):
        self.allRolls.append(pins)

    def scoreInFrame(self, frameStart):
        return self.allRolls[frameStart] + self.allRolls[frameStart+1]

    def isStrike(self, frameStart):
        return self.allRolls[frameStart] >= 10

    def isSpare(self, frameStart):
        return self.scoreInFrame(frameStart) >= 10

    def calculateScore(self):
        score = 0
        frameStart = 0
        while frameStart < len(self.allRolls):
            if self.isStrike(frameStart):
                score += self.allRolls[frameStart]
                score += self.scoreInFrame(frameStart+1)
                frameStart += 1
            if self.isSpare(frameStart):
                score += self.scoreInFrame(frameStart)
                score += self.allRolls[frameStart+2]
                frameStart += 2
            else:
                score += self.scoreInFrame(frameStart)
                frameStart += 2
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

    def testOneStrike(self):
        self.rollBalls(1,10)
        self.rollBalls(2,3)
        self.rollBalls(16,0)
        self.assertEqual(self.game.calculateScore(),22)

unittest.main()


