from enum import Enum
from threading import Thread

from rps_cv.core.config.coreconfig import CoreConfig

from rps_cv.core.utils.shape_interaction_rule import ShapeInteractionTable
from rps_cv.core.utils.turnresult import TurnResult


class GameState(Enum):
    NOT_STARTED = 0
    IN_PROGRESS = 1
    FINISHED = 2


class PlayerChoiceHandler(Thread):
    def __init__(self, gameService):
        super().__init__()
        self.gameService = gameService

    def run(self):
        self.gameService.nextRound()


class GameService:
    def __init__(self, playerService, computerService):
        self.playerService = playerService
        self.computerService = computerService

        self.ruleTable = ShapeInteractionTable()

        self.roundCount = 0
        self.defaultRoundNumber = CoreConfig['round_number']
        self.roundNumber = self.defaultRoundNumber

        self.roundState = GameState.NOT_STARTED
        self.gameState = GameState.NOT_STARTED


    def newGame(self):
        if self.gameState == GameState.IN_PROGRESS:
            return self.gameState
        self.gameState = GameState.IN_PROGRESS

        self.roundCount = 0
        self.roundNumber = self.defaultRoundNumber

        self.playerService.resetScore()
        self.computerService.resetScore()


    def nextRound(self):
        if self.roundState == GameState.IN_PROGRESS:
            return self.roundState
        if self.gameState == GameState.FINISHED:
            return self.gameState

        self.roundState = GameState.IN_PROGRESS

        self.roundCount += 1
        self.computerService.makeAChoice()

        # Warning: this absolutely needs to be stopped by getRoundWinner
        self.playerChoiceHandler = PlayerChoiceHandler(self)
        self.playerChoiceHandler.start()


    def getRoundWinner(self):
        if self.roundState != GameState.IN_PROGRESS:
            return None

        playerChoice = self.playerService.getChoice()
        computerChoice = self.computerService.getChoice()

        playerIs = self.ruleTable.getPlayerResult(playerChoice,
                                                computerChoice)

        if playerIs == TurnResult.WIN:
            self.playerService.setWin()
        elif playerIs == TurnResult.LOSE:
            self.computerService.setWin()

        self.roundState = GameState.NOT_STARTED
        return playerIs


    def getGameWinner(self):
        if self.gameState != GameState.IN_PROGRESS:
            return None

        if self.roundCount < self.roundNumber:
            return None

        if self.playerService.score > self.computerService.score:
            result = TurnResult.WIN
        elif self.playerService.score < self.computerService.score:
            result = TurnResult.LOSE
        else:
            raise ValueError('Game is a draw')

        self.gameState = GameState.FINISHED
        return result