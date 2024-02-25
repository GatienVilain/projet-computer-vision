from tkinter import *

from rps_cv.app.templates.layouts.computerlayout import ComputerLayout
from rps_cv.app.templates.layouts.playerlayout import PlayerLayout

from rps_cv.app.controller.computercontroller import ComputerController
from rps_cv.app.controller.playercontroller import PlayerController

from rps_cv.app.config.appconfig import AppConfig
from rps_cv.core.utils.turnresult import TurnResult


class MainFrame(Frame):
    def __init__(self, container, videoService, playerService, computerService):
        super().__init__(container)

        self.videoService = videoService
        self.playerService = playerService
        self.computerService = computerService

        self.video_width = videoService.width
        self.video_height = videoService.height

        self.__draw()

        self.controller = None
        self.playerController = PlayerController(self.roundLayout.playerLayout,
                                                 self.playerService,
                                                 self.videoService)
        self.computerController = ComputerController(self.roundLayout.computerLayout,
                                                     self.computerService)

        self.default_counter = AppConfig["round_duration"]
        self.counter = self.default_counter


    def __draw(self):
        self.__drawRoundLayout()
        self.__drawGameReview()


    def __drawRoundLayout(self):
        self.roundLayout = Frame(self)

        self.roundLayout.canvasRow = Frame(
            self.roundLayout,
            height=self.video_height
        )

        self.roundLayout.computerLayout = ComputerLayout(
            self.roundLayout.canvasRow,
            self.video_width,
            self.video_height
        )
        self.roundLayout.computerLayout.pack(side = LEFT)

        self.roundLayout.counterText = Label(
            self.roundLayout.canvasRow,
            text="Victoires",
            width=12
        )
        self.roundLayout.counterText.pack(side = LEFT)

        self.roundLayout.playerLayout = PlayerLayout(
            self.roundLayout.canvasRow,
            self.video_width,
            self.video_height
        )
        self.roundLayout.playerLayout.pack(side = RIGHT)

        self.roundLayout.canvasRow.pack()

        self.roundLayout.btn_nextround = Button(
            self.roundLayout,
            text="Tour suivant",
            width=50,
            command=self.nextRound
        )
        self.roundLayout.btn_nextround.pack(anchor = CENTER, expand=True)


    def __drawGameReview(self):
        self.gameReviewLayout = Frame(self)

        self.gameReviewLayout.label = Label(
            self.gameReviewLayout,
            text="Bienvenue dans le jeu de Pierre-Feuille-Ciseaux !",
            font='Arial 17 bold',
            height=10
        )
        self.gameReviewLayout.label.pack()

        self.gameReviewLayout.button = Button(
            self.gameReviewLayout,
            text="Nouvelle partie",
            command=self.newGame
        )
        self.gameReviewLayout.button.pack()

        self.gameReviewLayout.pack()


    def setController(self, computerController):
        self.controller = computerController


    def newGame(self):
        self.controller.newGame()


    def nextRound(self):
        self.controller.nextRound()


    def displayRoundLayout(self, delay):
        self.roundLayout.pack()
        self.gameReviewLayout.pack_forget()

        self.computerController.newRound()
        self.playerController.unsetRoundReview()
        self.updateCounter(self.default_counter)
        self.roundLayout.btn_nextround.pack_forget()

        self.after(delay, self.controller.getRoundWinner)


    def displayRoundReviewLayout(self):
        self.computerController.revealChoice()
        self.playerController.setRoundReview()
        self.showLabelResult()
        self.roundLayout.btn_nextround.pack(anchor = CENTER, expand=True)


    def displayGameReviewLayout(self):
        self.showGameResult()
        self.gameReviewLayout.pack()
        self.roundLayout.pack_forget()


    def updateCounter(self, counter = None):
        if counter: self.counter = counter
        self.roundLayout.counterText.config(text=str(self.counter))
        self.counter -= 1
        if self.counter > 0:
            self.after(1000, self.updateCounter)


    def showLabelResult(self):
        result = self.controller.roundResult
        if result == TurnResult.WIN:
            self.roundLayout.counterText.config(text="Victoire")
        elif result == TurnResult.LOSE:
            self.roundLayout.counterText.config(text="Défaite")
        elif result == TurnResult.DRAW:
            self.roundLayout.counterText.config(text="Égalité")


    def showGameResult(self):
        result = self.controller.gameResult
        text = ""
        if result == TurnResult.WIN:
            text = "Victoire, vous avez gagné avec " +\
                    str(self.playerService.getScore()) +\
                    " victoires contre " +\
                    str(self.computerService.getScore())
        elif result == TurnResult.LOSE:
            text = "Défaite, vous avez perdu avec " +\
                    str(self.playerService.getScore()) +\
                    " victoires contre " +\
                    str(self.computerService.getScore())
        elif result == TurnResult.DRAW:
            text = "Égalité, vous avez fait match nul avec " +\
                    str(self.playerService.getScore()) +\
                    " victoires contre " +\
                    str(self.computerService.getScore()) +\
                    ". Une partie supplémentaire pour vous départager ?"
        self.gameReviewLayout.label.config(text=text)