
from rps_cv.core.utils.shape import Shape
from rps_cv.core.utils.turnresult import TurnResult

class ShapeInteractionTable:
    def __init__(self):
        self.table = {
            # playerChoice: {computerChoice: result}
            Shape.ROCK: {
                Shape.ROCK: TurnResult.DRAW,
                Shape.PAPER: TurnResult.LOSE,
                Shape.SCISSORS: TurnResult.WIN
            },
            Shape.PAPER: {
                Shape.ROCK: TurnResult.WIN,
                Shape.PAPER: TurnResult.DRAW,
                Shape.SCISSORS: TurnResult.LOSE
            },
            Shape.SCISSORS: {
                Shape.ROCK: TurnResult.LOSE,
                Shape.PAPER: TurnResult.WIN,
                Shape.SCISSORS: TurnResult.DRAW
            }
        }

    def getPlayerResult(self, playerChoice, computerChoice):
        return self.table[playerChoice][computerChoice]