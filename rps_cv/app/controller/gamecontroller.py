import time

from rps_cv.core.service.gameservice import GameService, GameState

from rps_cv.app.config.appconfig import AppConfig
from rps_cv.app.templates.layouts.mainframe import MainFrame


class GameController:
    def __init__(self, mainframe, playerService, computerService):
        self.mainframe = mainframe
        self.mainframe.setController(self)

        self.playerService = playerService
        self.computerService = computerService
        self.gameService = GameService(self.playerService,
                                       self.computerService)

        self.roundDuration = AppConfig['round_duration']
        self.roundNumber = AppConfig['round_number']

        self.roundResult = None
        self.gameResult = None


    def newGame(self):
        if self.gameService.gameState == GameState.FINISHED: return self.getGameWinner()
        if self.gameService.gameState == GameState.NOT_STARTED:
            self.gameService.newGame(self.roundNumber)

        self.nextRound()


    def nextRound(self):
        if self.gameService.roundState == GameState.IN_PROGRESS: return
        if self.gameService.gameState == GameState.NOT_STARTED: return self.newGame()
        if self.gameService.gameState == GameState.FINISHED: return self.getGameWinner()

        self.gameService.nextRound()
        self.mainframe.displayRoundLayout(self.roundDuration * 1000)


    def getRoundWinner(self):
        self.roundResult = self.gameService.getRoundWinner()
        self.mainframe.displayRoundReviewLayout()


    def getGameWinner(self):
        self.gameResult = self.gameService.getGameWinner()
        self.mainframe.displayGameReviewLayout()

