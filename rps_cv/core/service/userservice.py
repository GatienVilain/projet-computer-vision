
from rps_cv.core.utils.shape import Shape

class UserService:
    def __init__(self):
        self.shape = Shape.NONE
        self.score = 0
        self.winner = False
        pass

    def resetScore(self):
        self.score = 0
        self.winner = False


    def getScore(self):
        return self.score


    def isWinner(self):
        return self.winner


    def setWin(self):
        self.score += 1
        self.winner = True


    def makeAChoice(self):
        self.winner = False
        pass


    def getChoice(self):
        return self.shape