import time

from rps_cv.core.service.gameservice import GameService, GameState

from rps_cv.app.config.appconfig import AppConfig
from rps_cv.app.templates.mainframe import MainFrame

# Todo move on App(TK) level

class GameController:
    def __init__(self, mainframe, playerService, computerService):
        self.playerService = playerService
        self.computerService = computerService
        self.gameService = GameService(self.playerService,
                                       self.computerService)

        self.mainframe = mainframe
        self.mainframe.setController(self)

        self.roundDuration = AppConfig['round_duration']

    def newGame(self):
        if self.gameService.gameState != GameState.IN_PROGRESS:
            self.gameService.newGame()

        self.nextRound()


    def nextRound(self):
        if self.gameService.roundState == GameState.IN_PROGRESS: return
        if self.gameService.gameState == GameState.FINISHED: self.getGameWinner()

        # self.mainframe.displayRoundLayout()
        self.gameService.nextRound()

        time.sleep(self.roundDuration) # in seconds
        self.getRoundWinner()


    def getRoundWinner(self):
        self.gameService.getGameWinner()
        # self.mainframe.displayRoundReviewLayout()


    def getGameWinner(self):
        self.gameService.getGameWinner()
        # self.mainframe.displayGameReviewLayout()

