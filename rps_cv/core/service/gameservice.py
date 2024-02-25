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
        self.gameService.playerService.makeAChoice()


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


    def newGame(self, defaultRoundNumber = None):
        if self.gameState != GameState.NOT_STARTED:
            print("Game already in progress")
            return self.gameState
        self.gameState = GameState.IN_PROGRESS

        self.roundCount = 0
        if defaultRoundNumber is not None:
            self.roundNumber = defaultRoundNumber
        else:
            self.roundNumber = self.defaultRoundNumber

        self.playerService.resetScore()
        self.computerService.resetScore()


    def nextRound(self):
        if self.roundState == GameState.IN_PROGRESS:
            print("Round already in progress")
            return self.roundState
        if self.gameState == GameState.FINISHED:
            print("Game already finished")
            return self.gameState
        if self.roundCount >= self.roundNumber:
            print("Game already finished")
            return self.gameState

        self.roundState = GameState.IN_PROGRESS

        self.roundCount += 1
        self.computerService.makeAChoice()

        # Warning: this absolutely needs to be stopped by getRoundWinner
        self.playerChoiceHandler = PlayerChoiceHandler(self)
        self.playerChoiceHandler.start()


    def getRoundWinner(self):
        if self.roundState != GameState.IN_PROGRESS:
            print("Round not in progress")
            return None

        playerChoice = self.playerService.getChoice()
        computerChoice = self.computerService.getChoice()

        playerIs = self.ruleTable.getPlayerResult(playerChoice,
                                                computerChoice)

        if playerIs == TurnResult.WIN:
            self.playerService.setWin()
        elif playerIs == TurnResult.LOSE:
            self.computerService.setWin()

        if self.roundCount >= self.roundNumber:
            self.gameState = GameState.FINISHED

        self.roundState = GameState.NOT_STARTED
        return playerIs


    def getGameWinner(self):
        if self.gameState != GameState.FINISHED:
            return None

        if self.playerService.score > self.computerService.score:
            result = TurnResult.WIN
        elif self.playerService.score < self.computerService.score:
            result = TurnResult.LOSE
        else:
            result = TurnResult.DRAW

        self.gameState = GameState.NOT_STARTED
        return result