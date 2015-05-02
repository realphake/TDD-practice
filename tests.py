import unittest

class BowlingGame():

    def __init__(self):
        self.allRolls = []

    def roll(self, pins):
        self.allRolls.append(pins)

    def calculateScore(self):
        score = 0
        i = 0
        while i < len(self.allRolls):
            frameScore = 0
            frameScore += self.allRolls[i]
            frameScore += self.allRolls[i+1]
            if frameScore >= 10:
                frameScore += self.allRolls[i+2]
            i += 2
            score += frameScore
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


